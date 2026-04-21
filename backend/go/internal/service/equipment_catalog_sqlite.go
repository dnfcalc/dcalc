package service

import (
	"database/sql"
	"fmt"
	"path/filepath"
	"strconv"
	"strings"

	_ "modernc.org/sqlite"
)

type SQLiteEquipmentCatalogRepository struct {
	projectRoot string
}

func NewSQLiteEquipmentCatalogRepository(projectRoot string) *SQLiteEquipmentCatalogRepository {
	return &SQLiteEquipmentCatalogRepository{projectRoot: projectRoot}
}

func (r *SQLiteEquipmentCatalogRepository) Catalog(_ string, equVersion string) (map[string]any, error) {
	if equVersion == "" {
		equVersion = "0"
	}

	dbPath := filepath.Join(r.projectRoot, "dataFiles", fmt.Sprintf("dcalc_%s.db", equVersion))
	db, err := sql.Open("sqlite", dbPath)
	if err != nil {
		return nil, err
	}
	defer db.Close()

	equips, err := queryEquipRows(db, "equ")
	if err != nil {
		return nil, err
	}
	stones, err := queryEquipRows(db, "stone")
	if err != nil {
		return nil, err
	}
	suits, err := querySuitRows(db)
	if err != nil {
		return nil, err
	}
	enchants, err := queryEnchantRows(db, "enchant")
	if err != nil {
		return nil, err
	}
	emblems, err := queryEnchantRows(db, "emblem")
	if err != nil {
		return nil, err
	}
	jades, err := queryJadeRows(db)
	if err != nil {
		return nil, err
	}

	return map[string]any{
		"equips":   equips,
		"suits":    suits,
		"stones":   stones,
		"enchants": enchants,
		"emblems":  emblems,
		"jades":    jades,
		"avatar":   map[string]any{},
		"options":  map[string]any{},
		"sundry":   []any{},
	}, nil
}

func queryEquipRows(db *sql.DB, table string) ([]map[string]any, error) {
	query := fmt.Sprintf("SELECT id,name,rarity,itemType,itemDetailType,Point,categorize,imageUrl,detail,bufferDetail,STR,INT,Vitality,Spirit,AtkP,AtkM,AtkI,SkillAttack,Attack,Buffer,suit FROM %s", table)
	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	result := make([]map[string]any, 0)
	for rows.Next() {
		var (
			id, name, rarity, itemType, itemDetailType, point, categorize, imageURL, detail, bufferDetail sql.NullString
			strV, intV, vitV, spiV, atkPV, atkMV, atkIV, skillAttackV, attackV, bufferV, suitV            sql.NullString
		)
		if err := rows.Scan(&id, &name, &rarity, &itemType, &itemDetailType, &point, &categorize, &imageURL, &detail, &bufferDetail, &strV, &intV, &vitV, &spiV, &atkPV, &atkMV, &atkIV, &skillAttackV, &attackV, &bufferV, &suitV); err != nil {
			return nil, err
		}

		entry := map[string]any{
			"id":             nullString(id),
			"name":           nullString(name),
			"rarity":         nullString(rarity),
			"itemType":       nullString(itemType),
			"itemDetailType": nullString(itemDetailType),
			"categorize":     nullString(categorize),
			"imageUrl":       nullString(imageURL),
			"detail":         nullString(detail),
			"bufferDetail":   nullString(bufferDetail),
			"Point":          numberListOrDefault(nullString(point)),
			"STR":            numberListOrDefault(nullString(strV)),
			"INT":            numberListOrDefault(nullString(intV)),
			"Vitality":       numberListOrDefault(nullString(vitV)),
			"Spirit":         numberListOrDefault(nullString(spiV)),
			"AtkP":           numberListOrDefault(nullString(atkPV)),
			"AtkM":           numberListOrDefault(nullString(atkMV)),
			"AtkI":           numberListOrDefault(nullString(atkIV)),
			"SkillAttack":    numberListOrDefault(nullString(skillAttackV)),
			"Attack":         numberListOrDefault(nullString(attackV)),
			"Buffer":         numberListOrDefault(nullString(bufferV)),
			"suit":           suitListOrDefault(nullString(suitV)),
		}

		maxAdaptation := 0
		for _, key := range []string{"Point", "STR", "INT", "Vitality", "Spirit", "AtkP", "AtkM", "AtkI", "SkillAttack", "Attack", "Buffer"} {
			if values, ok := entry[key].([]float64); ok && len(values)-1 > maxAdaptation {
				maxAdaptation = len(values) - 1
			}
		}
		entry["max_adaptation"] = maxAdaptation
		result = append(result, entry)
	}
	return result, rows.Err()
}

func querySuitRows(db *sql.DB) ([]map[string]any, error) {
	rows, err := db.Query("SELECT id,suitId,suitName,rarity,name,point,level,count,SkillAttack,Attack,Buffer,imageUrl,value,bufferValue,fame FROM suit")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	result := make([]map[string]any, 0)
	for rows.Next() {
		var (
			id, suitID, point, level, count, fame                sql.NullInt64
			suitName, rarity, name, imageURL, value, bufferValue sql.NullString
			skillAttack, attack, buffer                          sql.NullFloat64
		)
		if err := rows.Scan(&id, &suitID, &suitName, &rarity, &name, &point, &level, &count, &skillAttack, &attack, &buffer, &imageURL, &value, &bufferValue, &fame); err != nil {
			return nil, err
		}
		result = append(result, map[string]any{
			"id":          nullInt64(id),
			"suitId":      nullInt64(suitID),
			"suitName":    nullString(suitName),
			"rarity":      nullString(rarity),
			"name":        nullString(name),
			"point":       nullInt64(point),
			"level":       nullInt64(level),
			"count":       nullInt64(count),
			"SkillAttack": nullFloat64(skillAttack),
			"Attack":      nullFloat64(attack),
			"Buffer":      nullFloat64(buffer),
			"imageUrl":    nullString(imageURL),
			"value":       nullString(value),
			"bufferValue": nullString(bufferValue),
			"fame":        nullInt64(fame),
		})
	}
	return result, rows.Err()
}

func queryEnchantRows(db *sql.DB, table string) ([]map[string]any, error) {
	query := fmt.Sprintf("SELECT id,detail,categorize,itemType,fame,rarity FROM %s", table)
	rows, err := db.Query(query)
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	result := make([]map[string]any, 0)
	for rows.Next() {
		var id, fame sql.NullInt64
		var detail, categorize, itemType, rarity sql.NullString
		if err := rows.Scan(&id, &detail, &categorize, &itemType, &fame, &rarity); err != nil {
			return nil, err
		}
		result = append(result, map[string]any{
			"id":         nullInt64(id),
			"detail":     nullString(detail),
			"categorize": splitCSV(nullString(categorize)),
			"position":   splitCSV(nullString(itemType)),
			"fame":       nullInt64(fame),
			"rarity":     nullString(rarity),
		})
	}
	return result, rows.Err()
}

func queryJadeRows(db *sql.DB) ([]map[string]any, error) {
	rows, err := db.Query("SELECT id,name,min,max,unit,pre FROM jade")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	result := make([]map[string]any, 0)
	for rows.Next() {
		var id, minV, maxV sql.NullInt64
		var name, unit sql.NullString
		var pre sql.NullFloat64
		if err := rows.Scan(&id, &name, &minV, &maxV, &unit, &pre); err != nil {
			return nil, err
		}
		result = append(result, map[string]any{
			"id":   nullInt64(id),
			"name": nullString(name),
			"min":  nullInt64(minV),
			"max":  nullInt64(maxV),
			"unit": nullString(unit),
			"pre":  nullFloat64(pre),
		})
	}
	return result, rows.Err()
}

func numberListOrDefault(raw string) []float64 {
	raw = strings.TrimSpace(raw)
	if raw == "" {
		return []float64{0}
	}
	parts := strings.Split(raw, ",")
	result := make([]float64, 0, len(parts))
	for _, part := range parts {
		value, err := strconv.ParseFloat(strings.TrimSpace(part), 64)
		if err != nil {
			result = append(result, 0)
			continue
		}
		result = append(result, value)
	}
	if len(result) == 0 {
		return []float64{0}
	}
	return result
}

func suitListOrDefault(raw string) []string {
	raw = strings.TrimSpace(raw)
	if raw == "" {
		return []string{}
	}
	parts := strings.Split(raw, ",")
	result := make([]string, 0, len(parts))
	for _, part := range parts {
		part = strings.TrimSpace(part)
		if part == "" {
			continue
		}
		value, err := strconv.ParseFloat(part, 64)
		if err != nil {
			result = append(result, part)
			continue
		}
		result = append(result, strconv.Itoa(int(value)))
	}
	return result
}

func splitCSV(raw string) []string {
	raw = strings.TrimSpace(raw)
	if raw == "" {
		return []string{}
	}
	parts := strings.Split(raw, ",")
	result := make([]string, 0, len(parts))
	for _, part := range parts {
		part = strings.TrimSpace(part)
		if part != "" {
			result = append(result, part)
		}
	}
	return result
}

func nullString(value sql.NullString) string {
	if !value.Valid {
		return ""
	}
	return value.String
}

func nullInt64(value sql.NullInt64) int64 {
	if !value.Valid {
		return 0
	}
	return value.Int64
}

func nullFloat64(value sql.NullFloat64) float64 {
	if !value.Valid {
		return 0
	}
	return value.Float64
}
