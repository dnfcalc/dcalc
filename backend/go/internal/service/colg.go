package service

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"strconv"
	"strings"
	"time"

	"dcalc-go/internal/config"
)

type ColgService struct {
	cache  *Cache
	config config.Config
	client *http.Client
}

var regionMap = map[string]int{
	"跨1":  1,
	"跨2":  2,
	"跨3A": 3,
	"跨3B": 4,
	"跨4":  5,
	"跨5":  6,
	"跨6":  7,
	"跨7":  8,
}

func NewColgService(cache *Cache, cfg config.Config) *ColgService {
	return &ColgService{
		cache:  cache,
		config: cfg,
		client: &http.Client{Timeout: 12 * time.Second},
	}
}

func (s *ColgService) RealTimeGold(ctx context.Context) ([]map[string]any, error) {
	if s.config.ColgToken == "" {
		return nil, fmt.Errorf("COLG_TOKEN is required")
	}

	return GetOrLoad(s.cache, "colg:realtime", 30*time.Minute, func() ([]map[string]any, error) {
		result := make([]map[string]any, 0, len(regionMap))
		now := time.Now().Format("2006-01-02")
		for regionName, regionID := range regionMap {
			data, err := s.requestTrendData(ctx, regionID, now, now)
			if err != nil {
				return nil, err
			}
			xValues, _ := data["x"].([]any)
			yValues, _ := data["y"].([]any)
			if len(xValues) == 0 || len(yValues) == 0 {
				continue
			}
			result = append(result, map[string]any{
				"updataTime": formatBeijingTime(int64FromAny(xValues[len(xValues)-1])),
				"region":     regionName,
				"goldPrice":  float64FromAny(yValues[len(yValues)-1]),
			})
		}
		return result, nil
	})
}

func (s *ColgService) HistoryGold(ctx context.Context, region int, timeRange int) (map[string]any, error) {
	if s.config.ColgToken == "" {
		return nil, fmt.Errorf("COLG_TOKEN is required")
	}
	if timeRange <= 0 {
		timeRange = 7
	}

	regionName := ""
	for name, id := range regionMap {
		if id == region {
			regionName = name
			break
		}
	}
	if regionName == "" {
		return nil, fmt.Errorf("invalid region")
	}

	endDate := time.Now()
	startDate := endDate.AddDate(0, 0, -(timeRange - 1))
	trend, err := s.requestTrendData(ctx, region, startDate.Format("2006-01-02"), endDate.Format("2006-01-02"))
	if err != nil {
		return nil, err
	}

	xValues, _ := trend["x"].([]any)
	yValues, _ := trend["y"].([]any)
	y1Values, _ := trend["y1"].([]any)
	rows := make([]map[string]any, 0, len(xValues))
	minValue := 0.0
	maxValue := 0.0
	for index := range xValues {
		avg := float64FromAny(yValues[index])
		zero := float64FromAny(y1Values[index])
		if index == 0 || avg < minValue {
			minValue = avg
		}
		if zero < minValue {
			minValue = zero
		}
		if index == 0 || avg > maxValue {
			maxValue = avg
		}
		if zero > maxValue {
			maxValue = zero
		}
		rows = append(rows, map[string]any{
			"date": strings.Split(formatBeijingTime(int64FromAny(xValues[index])), " ")[0],
			"avg":  avg,
			"zero": zero,
		})
	}

	title := fmt.Sprintf("DNF%s近%d天金币价格趋势分析", regionName, timeRange)
	echarts := map[string]any{
		"title":   map[string]any{"text": title, "left": "center"},
		"toolbox": map[string]any{"feature": map[string]any{"saveAsImage": map[string]any{}, "dataView": map[string]any{"readOnly": true}, "magicType": map[string]any{"type": []string{"line", "bar"}}}},
		"tooltip": map[string]any{"trigger": "axis", "axisPointer": map[string]any{"type": "cross", "label": map[string]any{"backgroundColor": "#6a7985"}}},
		"legend":  map[string]any{"data": []string{"平均金价", "12时金价"}, "bottom": 0},
		"xAxis":   map[string]any{"type": "category", "name": "日期", "boundaryGap": false, "data": extractField(rows, "date")},
		"yAxis":   map[string]any{"type": "value", "name": "价格 (万金币/1人民币)", "min": floorToFive(minValue), "max": floorToFive(maxValue) + 5, "axisLabel": map[string]any{"formatter": "{value} 万金币"}},
		"series": []map[string]any{
			{"name": "平均金价", "type": "line", "smooth": true, "data": extractField(rows, "avg"), "markPoint": map[string]any{"data": []map[string]any{{"type": "max", "name": "最大值"}, {"type": "min", "name": "最小值"}}}},
			{"name": "12时金价", "type": "line", "smooth": true, "data": extractField(rows, "zero"), "markLine": map[string]any{"data": []map[string]any{{"type": "average", "name": "平均值"}}}},
		},
	}

	return map[string]any{"region": regionName, "data": rows, "echartsData": echarts}, nil
}

func (s *ColgService) OfficialGold(ctx context.Context) ([]map[string]any, error) {
	if s.config.HelperToken == "" || s.config.HelperID == "" {
		return nil, fmt.Errorf("HELPER_TOKEN and HELPER_ID are required")
	}

	return GetOrLoad(s.cache, "colg:official", 30*time.Minute, func() ([]map[string]any, error) {
		servers := []string{"1", "2", "3A", "3B", "4", "5", "6", "7"}
		result := make([]map[string]any, 0, len(servers))
		for _, server := range servers {
			data, err := s.requestOfficialGold(ctx, server)
			if err != nil {
				return nil, err
			}
			result = append(result, data)
		}
		return result, nil
	})
}

func (s *ColgService) requestTrendData(ctx context.Context, region int, startTime string, endTime string) (map[string]any, error) {
	payload := map[string]any{
		"token":      s.config.ColgToken,
		"area":       region,
		"time_type":  "other",
		"start_time": startTime,
		"end_time":   endTime,
	}
	body, err := json.Marshal(payload)
	if err != nil {
		return nil, err
	}

	req, err := http.NewRequestWithContext(ctx, http.MethodPost, "https://poservice.colg.cn/api/v1/trend/getCoinTrendDataKol", bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/json")

	resp, err := s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	content, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var payloadResp map[string]any
	if err := json.Unmarshal(content, &payloadResp); err != nil {
		return nil, err
	}
	data, _ := payloadResp["data"].(map[string]any)
	return data, nil
}

func (s *ColgService) requestOfficialGold(ctx context.Context, server string) (map[string]any, error) {
	form := url.Values{}
	form.Set("r", "godRank/godDealRank")
	form.Set("userId", s.config.HelperID)
	form.Set("token", s.config.HelperToken)
	form.Set("serverNo", server)

	req, err := http.NewRequestWithContext(ctx, http.MethodPost, "https://dzhu.qq.com/zangyi/activity/app", strings.NewReader(form.Encode()))
	if err != nil {
		return nil, err
	}
	req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

	resp, err := s.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	content, err := io.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	var payloadResp map[string]any
	if err := json.Unmarshal(content, &payloadResp); err != nil {
		return nil, err
	}
	data, _ := payloadResp["data"].(map[string]any)
	return map[string]any{
		"updataTime":      time.Now().Format("2006-01-02 15:04:05"),
		"region":          "跨" + server,
		"goldDealRank":    extractPrices(data["godDealRank"]),
		"goldTopDealRank": extractPrices(data["godTopDealRank"]),
	}, nil
}

func extractPrices(value any) []int {
	rows, _ := value.([]any)
	result := make([]int, 0, len(rows))
	for _, row := range rows {
		rowMap, _ := row.(map[string]any)
		result = append(result, intFromAnyString(rowMap["price"]))
	}
	return result
}

func extractField(rows []map[string]any, key string) []any {
	result := make([]any, 0, len(rows))
	for _, row := range rows {
		result = append(result, row[key])
	}
	return result
}

func formatBeijingTime(ts int64) string {
	return time.Unix(ts, 0).UTC().Add(8 * time.Hour).Format("2006-01-02 15:04:05")
}

func floorToFive(value float64) float64 {
	return float64(int(value/5) * 5)
}

func float64FromAny(value any) float64 {
	switch typed := value.(type) {
	case float64:
		return typed
	case float32:
		return float64(typed)
	case int:
		return float64(typed)
	case int64:
		return float64(typed)
	case json.Number:
		parsed, _ := typed.Float64()
		return parsed
	default:
		return 0
	}
}

func int64FromAny(value any) int64 {
	switch typed := value.(type) {
	case int64:
		return typed
	case int:
		return int64(typed)
	case float64:
		return int64(typed)
	case json.Number:
		parsed, _ := typed.Int64()
		return parsed
	default:
		return 0
	}
}

func intFromAnyString(value any) int {
	switch typed := value.(type) {
	case string:
		parsed, _ := strconv.Atoi(typed)
		return parsed
	default:
		return int(float64FromAny(value))
	}
}
