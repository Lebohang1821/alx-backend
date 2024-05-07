#!/usr/bin/env python3
"""First-In First-Out (FIFO) caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """It represents FIFO cache implementation
    using dictionary with FIFO removal 
    mechanism when limit is reached
    """
    def __init__(self):
        """It initializes the FIFO cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It stores item in cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """It retrieves an item from cache by key
        """
        return self.cache_data.get(key, None)
