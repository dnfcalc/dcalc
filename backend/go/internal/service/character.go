package service

import (
	"time"
)

type CharacterService struct {
	cache   *Cache
	factory CharacterFactory
}

func NewCharacterService(cache *Cache, factory CharacterFactory) *CharacterService {
	return &CharacterService{cache: cache, factory: factory}
}

func (s *CharacterService) StaticInfo(alter string, equVersion string) (map[string]any, error) {
	key := "character:static:" + alter + ":" + equVersion
	return GetOrLoad(s.cache, key, 15*time.Minute, func() (map[string]any, error) {
		return s.factory.CharacterInfo(alter, equVersion)
	})
}
