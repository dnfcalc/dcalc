package config

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
)

type Config struct {
	Port        string
	DebugMode   bool
	ColgToken   string
	HelperToken string
	HelperID    string
	PythonExec  string
	ProjectRoot string
}

func Load() (Config, error) {
	projectRoot, err := detectProjectRoot()
	if err != nil {
		return Config{}, err
	}

	return Config{
		Port:        envOrDefault("PORT", "27173"),
		DebugMode:   envBoolOrDefault("DEBUG_MODE", true),
		ColgToken:   os.Getenv("COLG_TOKEN"),
		HelperToken: os.Getenv("HELPER_TOKEN"),
		HelperID:    os.Getenv("HELPER_ID"),
		PythonExec:  pythonExecOrDefault(projectRoot),
		ProjectRoot: projectRoot,
	}, nil
}

func pythonExecOrDefault(projectRoot string) string {
	if value := os.Getenv("PYTHON_EXEC"); value != "" {
		return value
	}
	venvPython := filepath.Join(projectRoot, ".venv", "bin", "python")
	if fileExists(venvPython) {
		return venvPython
	}
	return "python3"
}

func detectProjectRoot() (string, error) {
	wd, err := os.Getwd()
	if err != nil {
		return "", err
	}

	current := wd
	for {
		if fileExists(filepath.Join(current, "openapi", "jobs.json")) {
			return current, nil
		}

		parent := filepath.Dir(current)
		if parent == current {
			return "", fmt.Errorf("unable to locate project root from %s", wd)
		}
		current = parent
	}
}

func fileExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}

func envOrDefault(key, fallback string) string {
	if value := os.Getenv(key); value != "" {
		return value
	}
	return fallback
}

func envBoolOrDefault(key string, fallback bool) bool {
	value := os.Getenv(key)
	if value == "" {
		return fallback
	}
	parsed, err := strconv.ParseBool(value)
	if err != nil {
		return fallback
	}
	return parsed
}
