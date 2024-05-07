#!/usr/bin/env python3
"""First-In First-Out (FIFO) caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """It represents an object that allows storing and
    retrieving items from dictionary wit FIFO
    removal mechanism when the limit is reached
    """
    def __init__(self):
        """It initializes FIFO cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It adds item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print("DISCARD:", first_key)

    def get(self, key):
        """It retrieves item by key
        """
        return self.cache_data.get(key, None)
