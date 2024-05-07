#!/usr/bin/env python3
"""Last-In First-Out (LIFO) caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """It represents object that allows storing and
    retrieving items from dictionary with a LIFO
    removal mechanism when limit is reached
    """
    def __init__(self):
        """It initializes LIFO cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It adds item in cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """It retrieves an item by key
        """
        return self.cache_data.get(key, None)
