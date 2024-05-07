#!/usr/bin/env python3
"""
Defines the class FIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Extends BaseCaching to implement put and get method:
        put method implements FIFO cache replacement when items
        in cache_data exceed MAX_ITEMS.
    """

    def __init__(self):
        """
        Initializes the cache with an ordered dict.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Adds an item to cache
        """
        if key is not None and item is not None:
            cache_len = len(self.cache_data)
            max_items = BaseCaching.MAX_ITEMS
            if cache_len >= max_items and key not in self.cache_data:
                discard = self.order[-1]
                del self.cache_data[discard]
                print('DISCARD: {}'.format(discard))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from cache
        """
        return self.cache_data.get(key)
