package service

import "errors"

var ErrNotImplemented = errors.New("calculation domain has not been migrated to Go yet")

type EquipmentCatalogRepository interface {
	Catalog(alter string, equVersion string) (map[string]any, error)
}

type CalcService struct {
	factory   CharacterFactory
	equipment EquipmentCatalogRepository
}

func NewCalcService(factory CharacterFactory, equipment EquipmentCatalogRepository) *CalcService {
	return &CalcService{factory: factory, equipment: equipment}
}

func (s *CalcService) CharacterInfo(alter string, equVersion string) (any, error) {
	return s.factory.CharacterInfo(alter, equVersion)
}

func (s *CalcService) Calculate(_ string, _ string, _ map[string]any) (any, error) {
	return nil, ErrNotImplemented
}

func (s *CalcService) SkillTree(_ string, _ string) (any, error) {
	return nil, ErrNotImplemented
}

func (s *CalcService) DNFHelper(_ string, _ string) (any, error) {
	return nil, ErrNotImplemented
}
