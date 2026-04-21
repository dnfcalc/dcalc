package service

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"os/exec"
	"path/filepath"
	"time"

	"dcalc-go/internal/config"
)

type CharacterSkillMeta struct {
	ID         string `json:"id"`
	Name       string `json:"name"`
	Type       string `json:"type"`
	LearnLv    int    `json:"learnLv"`
	MaxLearnLv int    `json:"maxLearnLv"`
	HasVP      bool   `json:"hasVP"`
	HasUP      bool   `json:"hasUP"`
	UUID       string `json:"uuid"`
}

type CharacterFactory interface {
	CharacterInfo(alter string, equVersion string) (map[string]any, error)
	CharacterSkills(alter string, equVersion string) ([]CharacterSkillMeta, error)
}

type PythonCharacterFactory struct {
	pythonExec  string
	projectRoot string
	scriptPath  string
}

func NewPythonCharacterFactory(cfg config.Config) *PythonCharacterFactory {
	return &PythonCharacterFactory{
		pythonExec:  cfg.PythonExec,
		projectRoot: cfg.ProjectRoot,
		scriptPath:  filepath.Join(cfg.ProjectRoot, "go", "python_bridge.py"),
	}
}

func (p *PythonCharacterFactory) CharacterInfo(alter string, equVersion string) (map[string]any, error) {
	result := map[string]any{}
	if err := p.invoke("character-info", alter, equVersion, &result); err != nil {
		return nil, err
	}
	return result, nil
}

func (p *PythonCharacterFactory) CharacterSkills(alter string, equVersion string) ([]CharacterSkillMeta, error) {
	var result []CharacterSkillMeta
	if err := p.invoke("character-skills", alter, equVersion, &result); err != nil {
		return nil, err
	}
	return result, nil
}

func (p *PythonCharacterFactory) invoke(command string, alter string, equVersion string, out any) error {
	if equVersion == "" {
		equVersion = "0"
	}

	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()

	cmd := exec.CommandContext(ctx, p.pythonExec, p.scriptPath, p.projectRoot, command, alter, equVersion)
	var stdout bytes.Buffer
	var stderr bytes.Buffer
	cmd.Stdout = &stdout
	cmd.Stderr = &stderr

	if err := cmd.Run(); err != nil {
		return fmt.Errorf("python bridge failed: %w, stdout=%s, stderr=%s", err, stdout.String(), stderr.String())
	}

	if err := json.Unmarshal(stdout.Bytes(), out); err != nil {
		return fmt.Errorf("unmarshal python bridge output: %w, raw=%s", err, stdout.String())
	}
	return nil
}
