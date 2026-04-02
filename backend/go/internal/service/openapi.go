package service

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
	"time"
)

var placeholderPattern = regexp.MustCompile(`<(?:(?:int)|(?:float\d*))>`)
var filenameJobPrefix = regexp.MustCompile(`^\d+(?:-\d+){0,2}`)

type OpenAPIService struct {
	projectRoot string
	cache       *Cache
	adventure   *AdventureService
}

func NewOpenAPIService(projectRoot string, cache *Cache, adventure *AdventureService) *OpenAPIService {
	return &OpenAPIService{projectRoot: projectRoot, cache: cache, adventure: adventure}
}

func (s *OpenAPIService) SearchSkills(skillName string) ([]map[string]any, error) {
	skills, err := GetOrLoad(s.cache, "openapi:skills", 30*time.Minute, func() ([]map[string]any, error) {
		var data []map[string]any
		if err := s.readJSON(filepath.Join(s.projectRoot, "openapi", "data", "skills.json"), &data); err != nil {
			return nil, err
		}
		return data, nil
	})
	if err != nil {
		return nil, err
	}

	normalized := normalizeWhitespace(skillName)
	if normalized == "" {
		return skills, nil
	}

	filtered := make([]map[string]any, 0)
	for _, skill := range skills {
		name, _ := skill["skillName"].(string)
		if strings.Contains(normalizeWhitespace(name), normalized) {
			filtered = append(filtered, skill)
		}
	}
	return filtered, nil
}

func (s *OpenAPIService) JobsInfo(jobName string) ([]map[string]string, error) {
	jobName = strings.NewReplacer("（", "(", "）", ")").Replace(jobName)
	result := make([]map[string]string, 0)
	for _, job := range s.adventure.Jobs() {
		for _, child := range job.Children {
			if jobName == "" || strings.Contains(child.Title, jobName) || strings.Contains(child.Name, jobName) {
				result = append(result, map[string]string{
					"jobId":       job.Name,
					"jobName":     job.Title,
					"jobGrowId":   child.Name,
					"jobGrowName": child.Title,
				})
			}
		}
	}
	return result, nil
}

func (s *OpenAPIService) SkillsByJob(jobID string, jobGrowID string) (any, error) {
	jobDir, jobGrowDir, err := s.adventure.ResolveDirectories(jobID, jobGrowID)
	if err != nil {
		return nil, err
	}

	var data any
	path := filepath.Join(s.projectRoot, "openapi", "data", jobDir, jobGrowDir, "cn", "skill_tree.json")
	if err := s.readJSON(path, &data); err != nil {
		return nil, err
	}
	return data, nil
}

func (s *OpenAPIService) SkillDetail(jobID string, jobGrowID string, skillID string, level *int) (any, error) {
	jobDir, jobGrowDir, err := s.adventure.ResolveDirectories(jobID, jobGrowID)
	if err != nil {
		return nil, err
	}

	var skillInfo map[string]any
	path := filepath.Join(s.projectRoot, "openapi", "data", jobDir, jobGrowDir, "cn", "skillDetail", skillID+".json")
	if err := s.readJSON(path, &skillInfo); err != nil {
		return nil, err
	}

	if levelInfo, ok := skillInfo["levelInfo"].(map[string]any); ok {
		if optionDesc, ok := levelInfo["optionDesc"].(string); ok {
			levelInfo["optionDesc"] = replacePlaceholders(optionDesc)
		}
	}

	if level == nil {
		return skillInfo, nil
	}

	maxLevel := intFromAny(skillInfo["maxLevel"])
	bounded := *level
	if bounded < 0 {
		bounded = 0
	}
	if maxLevel > 0 && bounded > maxLevel {
		bounded = maxLevel
	}

	levelInfo, ok := skillInfo["levelInfo"].(map[string]any)
	if !ok {
		return skillInfo, nil
	}
	rows, ok := levelInfo["rows"].([]any)
	if !ok {
		return skillInfo, nil
	}

	for _, row := range rows {
		rowMap, ok := row.(map[string]any)
		if !ok || intFromAny(rowMap["level"]) != bounded {
			continue
		}

		for key, value := range rowMap {
			levelInfo[key] = value
		}
		detail, _ := levelInfo["optionDesc"].(string)
		if optionValue, ok := levelInfo["optionValue"].(map[string]any); ok {
			for key, value := range optionValue {
				detail = strings.ReplaceAll(detail, "{"+key+"}", fmt.Sprint(value))
			}
		}
		levelInfo["detail"] = detail
		delete(levelInfo, "rows")
		skillInfo["attribute"] = levelInfo
		delete(skillInfo, "levelInfo")
		break
	}

	return skillInfo, nil
}

func (s *OpenAPIService) SkillDetailByAlter(alter string, skillID string, level int) (any, error) {
	jobDir, jobGrowDir, err := s.adventure.DirectoriesFromAlter(alter)
	if err != nil {
		return nil, err
	}
	return s.SkillDetail(jobDir, jobGrowDir, skillID, &level)
}

func (s *OpenAPIService) SkillDataSummary(job string, skills []string, weapons []string) ([]map[string]any, error) {
	job = strings.NewReplacer("（", "(", "）", ")").Replace(job)
	entries, err := os.ReadDir(filepath.Join(s.projectRoot, "openapi", "summary"))
	if err != nil {
		return nil, err
	}

	skillFilter := make(map[string]struct{})
	for _, skill := range skills {
		if skill != "" {
			skillFilter[skill] = struct{}{}
		}
	}
	weaponFilter := make(map[string]struct{})
	for _, weapon := range weapons {
		if weapon != "" {
			weaponFilter[weapon] = struct{}{}
		}
	}

	result := make([]map[string]any, 0)
	for _, entry := range entries {
		if entry.IsDir() || !strings.HasSuffix(entry.Name(), ".json") || !strings.Contains(entry.Name(), job) {
			continue
		}

		parts := strings.Split(strings.TrimSuffix(entry.Name(), ".json"), "_")
		weapon := "通用"
		if len(parts) > 1 && parts[len(parts)-1] != "" {
			weapon = parts[len(parts)-1]
		}
		if len(weaponFilter) > 0 {
			if _, ok := weaponFilter[weapon]; !ok {
				continue
			}
		}

		var rows []map[string]any
		if err := s.readJSON(filepath.Join(s.projectRoot, "openapi", "summary", entry.Name()), &rows); err != nil {
			return nil, err
		}

		jobTitle := strings.TrimPrefix(parts[0], filenameJobPrefix.FindString(parts[0]))
		for _, row := range rows {
			if len(skillFilter) > 0 {
				skillName, _ := row["技能名称"].(string)
				if _, ok := skillFilter[skillName]; !ok {
					continue
				}
			}
			copied := cloneMap(row)
			copied["武器类型"] = weapon
			copied["职业"] = jobTitle
			result = append(result, copied)
		}
	}

	return result, nil
}

func (s *OpenAPIService) readJSON(path string, dest any) error {
	content, err := os.ReadFile(path)
	if err != nil {
		return err
	}
	if err := json.Unmarshal(content, dest); err != nil {
		return fmt.Errorf("unmarshal %s: %w", path, err)
	}
	return nil
}

func replacePlaceholders(template string) string {
	count := 0
	return placeholderPattern.ReplaceAllStringFunc(template, func(_ string) string {
		count++
		return fmt.Sprintf("{value%d}", count)
	})
}

func normalizeWhitespace(value string) string {
	return strings.Join(strings.Fields(value), "")
}

func intFromAny(value any) int {
	switch typed := value.(type) {
	case int:
		return typed
	case int32:
		return int(typed)
	case int64:
		return int(typed)
	case float64:
		return int(typed)
	case float32:
		return int(typed)
	default:
		return 0
	}
}

func cloneMap(source map[string]any) map[string]any {
	cloned := make(map[string]any, len(source))
	for key, value := range source {
		cloned[key] = value
	}
	return cloned
}
