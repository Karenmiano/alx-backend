#!/usr/bin/env python3
"""
Defines the class LRUCache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Defines an LRU caching system
    """
    def __init__(self):
        """
        Initializes cache with a dict and order list to
        keep track of the usage of items.
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item to cache.
        """
        if key is not None and item is not None:
            cache_len = len(self.cache_data)
            max_items = BaseCaching.MAX_ITEMS
            if cache_len >= max_items and key not in self.cache_data:
                discard = self.order[0]
                print('DISCARD: {}'.format(discard))
                del self.cache_data[discard]
                del self.order[0]
            self.handle_key(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item from cache.
        """
        val = self.cache_data.get(key)
        if val is not None:
            self.handle_key(key)
        return val

    def handle_key(self, key):
        """
        Places recently used keys to the end of the order list.
        """
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
