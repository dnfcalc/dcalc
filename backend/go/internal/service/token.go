package service

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"time"
)

const tokenTTL = 6 * time.Hour

type TokenService struct {
	adventure *AdventureService
}

type AlterTokenPayload struct {
	Alter      string `json:"alter"`
	EquVersion string `json:"equVersion"`
	Time       int64  `json:"time"`
}

func NewTokenService(adventure *AdventureService) *TokenService {
	return &TokenService{adventure: adventure}
}

func (s *TokenService) Create(alterToken string, equVersion string) (string, error) {
	if equVersion == "" {
		equVersion = "0"
	}

	alter, err := s.adventure.AlterByToken(alterToken)
	if err != nil {
		return "", err
	}

	payload := AlterTokenPayload{
		Alter:      alter,
		EquVersion: equVersion,
		Time:       time.Now().UnixMilli(),
	}
	content, err := json.Marshal(payload)
	if err != nil {
		return "", err
	}

	return base64.RawURLEncoding.EncodeToString(content), nil
}

func (s *TokenService) Parse(token string) (AlterTokenPayload, error) {
	var payload AlterTokenPayload
	content, err := base64.RawURLEncoding.DecodeString(token)
	if err != nil {
		return payload, fmt.Errorf("decode token: %w", err)
	}
	if err := json.Unmarshal(content, &payload); err != nil {
		return payload, fmt.Errorf("unmarshal token: %w", err)
	}
	if payload.Time <= 0 || time.Since(time.UnixMilli(payload.Time)) > tokenTTL {
		return AlterTokenPayload{}, fmt.Errorf("token expired")
	}
	return payload, nil
}
