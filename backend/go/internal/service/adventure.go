package service

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"time"
)

type AdventureService struct {
	projectRoot string
	cache       *Cache
	jobs        []Job
	tokenToJob  map[string]string
}

type Job struct {
	Name     string     `json:"name"`
	JobID    string     `json:"jobId"`
	Title    string     `json:"title"`
	Children []JobChild `json:"children"`
}

type JobChild struct {
	Name      string `json:"name"`
	JobGrowID string `json:"jobGrowId"`
	Title     string `json:"title"`
}

type AdventureParent struct {
	ID       int              `json:"id"`
	Name     string           `json:"name"`
	Title    string           `json:"title"`
	Children []AdventureChild `json:"children"`
}

type AdventureChild struct {
	ID    int    `json:"id"`
	Name  string `json:"name"`
	Title string `json:"title"`
	Open  bool   `json:"open"`
	Value string `json:"value"`
}

func NewAdventureService(projectRoot string, cache *Cache) (*AdventureService, error) {
	jobsPath := filepath.Join(projectRoot, "openapi", "jobs.json")
	content, err := os.ReadFile(jobsPath)
	if err != nil {
		return nil, err
	}

	var jobs []Job
	if err := json.Unmarshal(content, &jobs); err != nil {
		return nil, err
	}

	svc := &AdventureService{
		projectRoot: projectRoot,
		cache:       cache,
		jobs:        jobs,
		tokenToJob:  make(map[string]string),
	}

	for parentIndex, parent := range jobs {
		for childIndex, child := range parent.Children {
			token := base64.StdEncoding.EncodeToString([]byte(fmt.Sprintf("%02d%02d00", parentIndex, childIndex)))
			svc.tokenToJob[token] = "GF." + parent.Name + "." + child.Name
		}
	}

	return svc, nil
}

func (s *AdventureService) Jobs() []Job {
	jobs := make([]Job, len(s.jobs))
	copy(jobs, s.jobs)
	return jobs
}

func (s *AdventureService) AdventureList() ([]AdventureParent, error) {
	return GetOrLoad(s.cache, "adventure:list", 10*time.Minute, func() ([]AdventureParent, error) {
		result := make([]AdventureParent, 0, len(s.jobs))
		for parentIndex, parent := range s.jobs {
			children := make([]AdventureChild, 0, len(parent.Children))
			for childIndex, child := range parent.Children {
				children = append(children, AdventureChild{
					ID:    childIndex,
					Name:  child.Name,
					Title: child.Title,
					Open:  true,
					Value: base64.StdEncoding.EncodeToString([]byte(fmt.Sprintf("%02d%02d00", parentIndex, childIndex))),
				})
			}
			result = append(result, AdventureParent{
				ID:       parentIndex,
				Name:     parent.Name,
				Title:    parent.Title,
				Children: children,
			})
		}
		return result, nil
	})
}

func (s *AdventureService) AlterByToken(token string) (string, error) {
	alter, ok := s.tokenToJob[token]
	if !ok {
		return "", fmt.Errorf("invalid adventure token")
	}
	return alter, nil
}

func (s *AdventureService) ResolveDirectories(jobIdentifier string, jobGrowIdentifier string) (string, string, error) {
	for _, job := range s.jobs {
		jobMatched := jobIdentifier == job.Name || jobIdentifier == job.JobID
		if !jobMatched {
			continue
		}
		for _, child := range job.Children {
			if jobGrowIdentifier == child.Name || jobGrowIdentifier == child.JobGrowID {
				return job.Name, child.Name, nil
			}
		}
	}
	return "", "", fmt.Errorf("unknown job path: %s/%s", jobIdentifier, jobGrowIdentifier)
}

func (s *AdventureService) DirectoriesFromAlter(alter string) (string, string, error) {
	parts := strings.Split(alter, ".")
	if len(parts) != 3 || parts[0] != "GF" {
		return "", "", fmt.Errorf("invalid alter value: %s", alter)
	}
	return parts[1], parts[2], nil
}
