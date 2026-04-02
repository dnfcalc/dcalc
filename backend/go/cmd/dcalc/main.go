package main

import (
	"log"
	"net/http"

	"dcalc-go/internal/config"
	"dcalc-go/internal/httpserver"
	"dcalc-go/internal/service"
)

func main() {
	cfg, err := config.Load()
	if err != nil {
		log.Fatalf("load config: %v", err)
	}

	cache := service.NewCache()
	adventureService, err := service.NewAdventureService(cfg.ProjectRoot, cache)
	if err != nil {
		log.Fatalf("load adventure data: %v", err)
	}

	openAPIService := service.NewOpenAPIService(cfg.ProjectRoot, cache, adventureService)
	colgService := service.NewColgService(cache, cfg)
	tokenService := service.NewTokenService(adventureService)
	characterFactory := service.NewPythonCharacterFactory(cfg)
	characterService := service.NewCharacterService(cache, characterFactory)
	skillTreeService, err := service.NewSkillTreeService(cfg.ProjectRoot, adventureService, characterFactory)
	if err != nil {
		log.Fatalf("load skill tree service: %v", err)
	}
	equipmentRepository := service.NewSQLiteEquipmentCatalogRepository(cfg.ProjectRoot)
	calcService := service.NewCalcService(characterFactory, equipmentRepository)

	router := httpserver.NewRouter(httpserver.Dependencies{
		Config:           cfg,
		AdventureService: adventureService,
		OpenAPIService:   openAPIService,
		ColgService:      colgService,
		TokenService:     tokenService,
		CharacterService: characterService,
		SkillTreeService: skillTreeService,
		CalcService:      calcService,
	})

	addr := ":" + cfg.Port
	log.Printf("dcalc go server listening on %s", addr)
	if err := http.ListenAndServe(addr, router); err != nil {
		log.Fatalf("listen and serve: %v", err)
	}
}
