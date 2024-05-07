#!/usr/bin/env python3
"""It caches module implementing basic cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """It represents basic cache implementation
    using dictionary
    """
    def put(self, key, item):
        """It stores item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """It retrieves item from cache by key
        """
        return self.cache_data.get(key, None)
