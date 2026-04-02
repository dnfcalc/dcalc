package service

import (
	"sync"
	"time"
)

type Cache struct {
	mu    sync.RWMutex
	items map[string]cacheItem
}

type cacheItem struct {
	value     any
	expiresAt time.Time
}

func NewCache() *Cache {
	return &Cache{items: make(map[string]cacheItem)}
}

func GetOrLoad[T any](cache *Cache, key string, ttl time.Duration, loader func() (T, error)) (T, error) {
	var zero T

	cache.mu.RLock()
	item, ok := cache.items[key]
	cache.mu.RUnlock()
	if ok && (item.expiresAt.IsZero() || item.expiresAt.After(time.Now())) {
		if value, castOK := item.value.(T); castOK {
			return value, nil
		}
	}

	value, err := loader()
	if err != nil {
		return zero, err
	}

	cache.mu.Lock()
	cache.items[key] = cacheItem{value: value, expiresAt: time.Now().Add(ttl)}
	cache.mu.Unlock()

	return value, nil
}
