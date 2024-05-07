#!/usr/bin/env python3
"""Most Recently Used (MRU) caching module
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """It represents object that allows storing and
    retrieving items from dictionary with MRU
    removal mechanism when limit is reached
    """
    def __init__(self):
        """It initializes MRU cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """It adds an item in cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """It retrieves item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
