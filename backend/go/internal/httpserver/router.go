package httpserver

import (
	"encoding/json"
	"errors"
	"io"
	"net/http"
	"strconv"
	"strings"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	"dcalc-go/internal/config"
	"dcalc-go/internal/model"
	"dcalc-go/internal/service"
)

type Dependencies struct {
	Config           config.Config
	AdventureService *service.AdventureService
	OpenAPIService   *service.OpenAPIService
	ColgService      *service.ColgService
	TokenService     *service.TokenService
	CharacterService *service.CharacterService
	SkillTreeService *service.SkillTreeService
	CalcService      *service.CalcService
}

func NewRouter(dep Dependencies) http.Handler {
	r := chi.NewRouter()
	r.Use(middleware.RequestID)
	r.Use(middleware.RealIP)
	r.Use(middleware.Logger)
	r.Use(middleware.Recoverer)
	r.Use(middleware.Compress(5, "application/json"))
	r.Use(cors)

	r.Get("/healthz", func(w http.ResponseWriter, _ *http.Request) {
		writeJSON(w, http.StatusOK, model.Success(map[string]any{"service": "dcalc-go", "debug": dep.Config.DebugMode}))
	})

	r.Route("/api", func(r chi.Router) {
		r.Get("/adventure", func(w http.ResponseWriter, r *http.Request) {
			data, err := dep.AdventureService.AdventureList()
			if err != nil {
				writeError(w, http.StatusInternalServerError, err)
				return
			}
			writeJSON(w, http.StatusOK, model.Success(data))
		})

		r.Get("/token/get/{alter}", func(w http.ResponseWriter, r *http.Request) {
			token, err := dep.TokenService.Create(chi.URLParam(r, "alter"), r.URL.Query().Get("equVersion"))
			if err != nil {
				writeJSON(w, http.StatusBadRequest, model.Error(400, err.Error(), nil))
				return
			}
			writeJSON(w, http.StatusOK, model.Success(token))
		})

		r.Get("/character", func(w http.ResponseWriter, r *http.Request) {
			payload, ok := requireAlterToken(w, r, dep.TokenService)
			if !ok {
				return
			}
			data, err := dep.CharacterService.StaticInfo(payload.Alter, payload.EquVersion)
			if err != nil {
				writeError(w, http.StatusInternalServerError, err)
				return
			}
			writeJSON(w, http.StatusOK, model.Success(data))
		})

		r.Post("/calc", func(w http.ResponseWriter, r *http.Request) {
			payload, ok := requireAlterToken(w, r, dep.TokenService)
			if !ok {
				return
			}

			var body map[string]any
			if err := json.NewDecoder(r.Body).Decode(&body); err != nil && !errors.Is(err, io.EOF) && !errors.Is(err, http.ErrBodyNotAllowed) {
				writeJSON(w, http.StatusBadRequest, model.Error(400, "invalid request body", nil))
				return
			}

			data, err := dep.CalcService.Calculate(payload.Alter, payload.EquVersion, body)
			if err != nil {
				writeNotImplemented(w, err)
				return
			}
			writeJSON(w, http.StatusOK, model.Success(data))
		})

		r.Get("/skill/{skillId}/{level}", func(w http.ResponseWriter, r *http.Request) {
			payload, ok := requireAlterToken(w, r, dep.TokenService)
			if !ok {
				return
			}
			level, err := strconv.Atoi(chi.URLParam(r, "level"))
			if err != nil {
				writeJSON(w, http.StatusBadRequest, model.Error(400, "level must be an integer", nil))
				return
			}
			data, err := dep.OpenAPIService.SkillDetailByAlter(payload.Alter, chi.URLParam(r, "skillId"), level)
			if err != nil {
				writeJSON(w, http.StatusNotFound, model.Error(404, err.Error(), nil))
				return
			}
			writeJSON(w, http.StatusOK, model.Success(data))
		})

		r.Get("/dnfhelper/{uid}/", func(w http.ResponseWriter, _ *http.Request) {
			writeJSON(w, http.StatusNotImplemented, model.Error(501, "dnfhelper integration is pending migration", nil))
		})

		r.Post("/skillTree/", func(w http.ResponseWriter, r *http.Request) {
			payload, ok := requireAlterToken(w, r, dep.TokenService)
			if !ok {
				return
			}

			var body map[string]any
			if err := json.NewDecoder(r.Body).Decode(&body); err != nil && !errors.Is(err, io.EOF) {
				writeJSON(w, http.StatusBadRequest, model.Error(400, "invalid request body", nil))
				return
			}
			code, _ := body["code"].(string)
			result, err := dep.SkillTreeService.Parse(code, payload.EquVersion)
			if err != nil {
				writeJSON(w, http.StatusInternalServerError, model.Error(500, "解析技能加点失败", nil))
				return
			}
			if result.Job["class"] != payload.Alter {
				writeJSON(w, http.StatusInternalServerError, model.Error(500, "技能加点代码职业与登录职业不匹配", nil))
				return
			}
			writeJSON(w, http.StatusOK, model.Success(result))
		})

		r.Route("/open", func(r chi.Router) {
			r.Get("/skills/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.OpenAPIService.SearchSkills(r.URL.Query().Get("skillName"))
				if err != nil {
					writeError(w, http.StatusInternalServerError, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/jobInfo/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.OpenAPIService.JobsInfo(r.URL.Query().Get("jobName"))
				if err != nil {
					writeError(w, http.StatusInternalServerError, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/skillData/summary/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.OpenAPIService.SkillDataSummary(
					r.URL.Query().Get("job"),
					splitCSV(r.URL.Query().Get("skills")),
					splitCSV(r.URL.Query().Get("weapons")),
				)
				if err != nil {
					writeError(w, http.StatusInternalServerError, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/gold/realtime/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.ColgService.RealTimeGold(r.Context())
				if err != nil {
					writeError(w, http.StatusBadGateway, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/gold/history/", func(w http.ResponseWriter, r *http.Request) {
				region, err := strconv.Atoi(r.URL.Query().Get("region"))
				if err != nil {
					writeJSON(w, http.StatusBadRequest, model.Error(400, "region must be an integer", nil))
					return
				}
				timeRange := 7
				if raw := r.URL.Query().Get("timeRange"); raw != "" {
					parsed, err := strconv.Atoi(raw)
					if err != nil {
						writeJSON(w, http.StatusBadRequest, model.Error(400, "timeRange must be an integer", nil))
						return
					}
					timeRange = parsed
				}

				data, err := dep.ColgService.HistoryGold(r.Context(), region, timeRange)
				if err != nil {
					writeJSON(w, http.StatusBadRequest, model.Error(404, err.Error(), nil))
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/gold/official/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.ColgService.OfficialGold(r.Context())
				if err != nil {
					writeError(w, http.StatusBadGateway, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/{jobId}/{jobGrowId}/skills/", func(w http.ResponseWriter, r *http.Request) {
				data, err := dep.OpenAPIService.SkillsByJob(chi.URLParam(r, "jobId"), chi.URLParam(r, "jobGrowId"))
				if err != nil {
					writeError(w, http.StatusNotFound, err)
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})

			r.Get("/{jobId}/{jobGrowId}/{skillId}/", func(w http.ResponseWriter, r *http.Request) {
				var level *int
				if raw := r.URL.Query().Get("level"); raw != "" {
					parsed, err := strconv.Atoi(raw)
					if err != nil {
						writeJSON(w, http.StatusBadRequest, model.Error(400, "level must be an integer", nil))
						return
					}
					level = &parsed
				}
				data, err := dep.OpenAPIService.SkillDetail(chi.URLParam(r, "jobId"), chi.URLParam(r, "jobGrowId"), chi.URLParam(r, "skillId"), level)
				if err != nil {
					writeJSON(w, http.StatusNotFound, model.Error(404, err.Error(), nil))
					return
				}
				writeJSON(w, http.StatusOK, model.Success(data))
			})
		})
	})

	return r
}

func requireAlterToken(w http.ResponseWriter, r *http.Request, tokens *service.TokenService) (service.AlterTokenPayload, bool) {
	token := r.Header.Get("alter_token")
	if token == "" {
		writeJSON(w, http.StatusUnauthorized, model.Error(401, "missing alter_token header", nil))
		return service.AlterTokenPayload{}, false
	}
	payload, err := tokens.Parse(token)
	if err != nil {
		writeJSON(w, http.StatusUnauthorized, model.Error(401, "invalid alter_token header", nil))
		return service.AlterTokenPayload{}, false
	}
	return payload, true
}

func writeNotImplemented(w http.ResponseWriter, err error) {
	writeJSON(w, http.StatusNotImplemented, model.Error(501, err.Error(), nil))
}

func writeError(w http.ResponseWriter, status int, err error) {
	writeJSON(w, status, model.Error(status, err.Error(), nil))
}

func writeJSON(w http.ResponseWriter, status int, payload model.Envelope) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(payload)
}

func cors(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, alter_token")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
		if r.Method == http.MethodOptions {
			w.WriteHeader(http.StatusNoContent)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func splitCSV(value string) []string {
	if value == "" {
		return nil
	}
	parts := strings.Split(value, ",")
	result := make([]string, 0, len(parts))
	for _, part := range parts {
		trimmed := strings.TrimSpace(part)
		if trimmed != "" {
			result = append(result, trimmed)
		}
	}
	return result
}
