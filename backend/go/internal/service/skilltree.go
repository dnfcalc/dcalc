package service

import (
	"bytes"
	"compress/zlib"
	"encoding/base64"
	"encoding/binary"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
	"unicode/utf16"
)

type SkillTreeService struct {
	adventure  *AdventureService
	factory    CharacterFactory
	indexToUID map[int][]string
}

type decodedSkillCode struct {
	Header       skillCodeHeader
	Skills       []skillLearnItem
	Evolutions   []skillChoice
	Enhancements []skillChoice
}

type skillCodeHeader struct {
	Name     string
	Level    int
	JobBytes [2]int
}

type skillLearnItem struct {
	SkillIndex int
	Level      int
	SkillType  int
}

type skillChoice struct {
	SkillIndex int
	Type       int
}

type LearnedSkill struct {
	Lv   int    `json:"lv"`
	Up   int    `json:"up"`
	VP   int    `json:"vp"`
	Name string `json:"name"`
}

type SkillTreeResult struct {
	Name   string                  `json:"name"`
	Level  int                     `json:"level"`
	Job    map[string]string       `json:"job"`
	Skills map[string]LearnedSkill `json:"skills"`
}

var roleMap = map[int]int{
	0:  0,
	1:  3,
	2:  4,
	3:  7,
	4:  8,
	5:  5,
	6:  10,
	7:  2,
	8:  6,
	9:  15,
	10: 15,
	11: 1,
	12: 11,
	13: 12,
	14: 9,
	15: 13,
	16: 14,
}

func NewSkillTreeService(projectRoot string, adventure *AdventureService, factory CharacterFactory) (*SkillTreeService, error) {
	indexToUID, err := loadSkillIndexMap(filepath.Join(projectRoot, "dataFiles", "skillMap.json"))
	if err != nil {
		return nil, err
	}
	return &SkillTreeService{adventure: adventure, factory: factory, indexToUID: indexToUID}, nil
}

func (s *SkillTreeService) Parse(code string, equVersion string) (SkillTreeResult, error) {
	decoded, err := decodeSkillCode(code)
	if err != nil {
		return SkillTreeResult{}, err
	}

	alter, err := alterFromJobBytes(decoded.Header.JobBytes[0], decoded.Header.JobBytes[1], s.adventure)
	if err != nil {
		return SkillTreeResult{}, err
	}

	skills, err := s.factory.CharacterSkills(alter, equVersion)
	if err != nil {
		return SkillTreeResult{}, err
	}

	skillByUUID := make(map[string][]CharacterSkillMeta)
	for _, skill := range skills {
		skillByUUID[skill.UUID] = append(skillByUUID[skill.UUID], skill)
	}

	indexCandidates := make(map[int][]CharacterSkillMeta)
	for _, item := range decoded.Skills {
		if _, exists := indexCandidates[item.SkillIndex]; exists {
			continue
		}
		indexCandidates[item.SkillIndex] = s.buildCandidates(item.SkillIndex, skillByUUID)
	}

	learned := make(map[string]LearnedSkill)
	for _, item := range decoded.Skills {
		candidates := indexCandidates[item.SkillIndex]
		chosen := chooseSkillCandidate(candidates, item.SkillType)
		if chosen == nil {
			continue
		}
		current, exists := learned[chosen.ID]
		if !exists || current.Lv < item.Level {
			learned[chosen.ID] = LearnedSkill{Lv: item.Level, Up: 0, VP: 0, Name: chosen.Name}
		}
	}

	for _, evo := range decoded.Evolutions {
		for _, skill := range indexCandidates[evo.SkillIndex] {
			if !skill.HasVP {
				continue
			}
			if learnedSkill, ok := learned[skill.ID]; ok {
				learnedSkill.VP = evo.Type
				learned[skill.ID] = learnedSkill
			}
		}
	}

	for _, up := range decoded.Enhancements {
		for _, skill := range indexCandidates[up.SkillIndex] {
			if !skill.HasUP {
				continue
			}
			if learnedSkill, ok := learned[skill.ID]; ok {
				learnedSkill.Up = up.Type
				learned[skill.ID] = learnedSkill
			}
		}
	}

	for _, skill := range skills {
		if _, exists := learned[skill.ID]; exists {
			continue
		}
		level := 0
		if skill.LearnLv == 50 || skill.LearnLv == 85 || skill.Name == "基础精通" {
			level = skill.MaxLearnLv
		}
		learned[skill.ID] = LearnedSkill{Lv: level, Up: 0, VP: 0, Name: skill.Name}
	}

	return SkillTreeResult{
		Name:   decoded.Header.Name,
		Level:  decoded.Header.Level,
		Job:    map[string]string{"class": alter},
		Skills: learned,
	}, nil
}

func (s *SkillTreeService) buildCandidates(index int, skillByUUID map[string][]CharacterSkillMeta) []CharacterSkillMeta {
	uuids := s.indexToUID[index]
	seen := make(map[string]struct{})
	candidates := make([]CharacterSkillMeta, 0)
	for _, uuid := range uuids {
		for _, skill := range skillByUUID[uuid] {
			if _, exists := seen[skill.ID]; exists {
				continue
			}
			seen[skill.ID] = struct{}{}
			candidates = append(candidates, skill)
		}
	}
	if len(candidates) > 1 {
		filtered := make([]CharacterSkillMeta, 0)
		for _, skill := range candidates {
			if skill.LearnLv == 50 || skill.LearnLv == 85 {
				continue
			}
			filtered = append(filtered, skill)
		}
		if len(filtered) > 0 {
			return filtered
		}
	}
	return candidates
}

func chooseSkillCandidate(candidates []CharacterSkillMeta, skillType int) *CharacterSkillMeta {
	if len(candidates) == 0 {
		return nil
	}
	if len(candidates) == 1 {
		return &candidates[0]
	}
	wantedType := "passive"
	if skillType == 1 {
		wantedType = "active"
	}
	for i := range candidates {
		if candidates[i].Type == wantedType {
			return &candidates[i]
		}
	}
	return &candidates[0]
}

func loadSkillIndexMap(path string) (map[int][]string, error) {
	content, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}

	uuidToIndexes := map[string][]int{}
	if err := json.Unmarshal(content, &uuidToIndexes); err != nil {
		return nil, err
	}

	indexToUUID := make(map[int][]string)
	for uuid, indexes := range uuidToIndexes {
		for _, idx := range indexes {
			indexToUUID[idx] = append(indexToUUID[idx], uuid)
		}
	}
	return indexToUUID, nil
}

func alterFromJobBytes(roleByte int, jobByte int, adventure *AdventureService) (string, error) {
	parent, ok := roleMap[roleByte]
	if !ok {
		return "", fmt.Errorf("unsupported role byte: %d", roleByte)
	}

	jobID := jobByte - 1
	if roleByte == 9 {
		jobID = 1
	}
	if roleByte == 10 {
		jobID = 0
	}

	token := base64.StdEncoding.EncodeToString([]byte(fmt.Sprintf("%02d%02d00", parent, jobID)))
	return adventure.AlterByToken(token)
}

func decodeSkillCode(encoded string) (decodedSkillCode, error) {
	result := decodedSkillCode{}

	compressed, err := base64.StdEncoding.DecodeString(encoded)
	if err != nil {
		return result, fmt.Errorf("decode base64: %w", err)
	}

	r, err := zlib.NewReader(bytes.NewReader(compressed))
	if err != nil {
		return result, fmt.Errorf("create zlib reader: %w", err)
	}
	defer r.Close()

	raw, err := io.ReadAll(r)
	if err != nil {
		return result, fmt.Errorf("read zlib stream: %w", err)
	}
	if len(raw) < 14 {
		return result, fmt.Errorf("invalid skill code payload")
	}

	nameLen := int(raw[13])
	if 14+nameLen > len(raw) {
		return result, fmt.Errorf("invalid name length in skill code")
	}

	result.Header = skillCodeHeader{
		Name:     decodeUTF16LE(raw[14 : 14+nameLen]),
		Level:    int(raw[5]),
		JobBytes: [2]int{int(raw[2]), int(raw[3])},
	}

	data := raw[14+nameLen:]
	if len(data)%2 == 1 {
		data = append(data, 0)
	}

	uint16s := make([]uint16, 0, len(data)/2)
	for i := 0; i < len(data); i += 2 {
		uint16s = append(uint16s, binary.LittleEndian.Uint16(data[i:i+2]))
	}
	if len(uint16s) == 0 {
		return result, nil
	}

	high := make([]byte, len(uint16s))
	low := make([]byte, len(uint16s))
	for i, value := range uint16s {
		high[i] = byte(value >> 8)
		low[i] = byte(value & 0xFF)
	}

	pairCount := int(high[0])
	for i := 0; i < pairCount; i++ {
		base := 1 + i*2
		if base+1 >= len(high) {
			break
		}
		result.Skills = append(result.Skills, skillLearnItem{
			SkillIndex: int(high[base]),
			Level:      int(high[base+1]),
			SkillType:  int(low[base+1]),
		})
	}

	sectionStart := (1 + pairCount*2) * 2
	if sectionStart >= len(data) {
		return result, nil
	}
	sec2 := data[sectionStart:]
	if len(sec2) < 2 {
		return result, nil
	}

	offset := 1
	evoCount := int(sec2[offset])
	offset++
	for i := 0; i < evoCount; i++ {
		if offset+3 > len(sec2) {
			break
		}
		result.Evolutions = append(result.Evolutions, skillChoice{
			SkillIndex: int(sec2[offset]),
			Type:       int(sec2[offset+2]) + 1,
		})
		offset += 3
	}

	if offset >= len(sec2) {
		return result, nil
	}
	enhCount := int(sec2[offset])
	offset++
	for i := 0; i < enhCount; i++ {
		if offset+3 > len(sec2) {
			break
		}
		result.Enhancements = append(result.Enhancements, skillChoice{
			SkillIndex: int(sec2[offset]),
			Type:       int(sec2[offset+2]) + 1,
		})
		offset += 3
	}

	return result, nil
}

func decodeUTF16LE(value []byte) string {
	if len(value)%2 == 1 {
		value = append(value, 0)
	}
	words := make([]uint16, 0, len(value)/2)
	for i := 0; i < len(value); i += 2 {
		words = append(words, binary.LittleEndian.Uint16(value[i:i+2]))
	}
	return strings.TrimSpace(string(utf16.Decode(words)))
}
