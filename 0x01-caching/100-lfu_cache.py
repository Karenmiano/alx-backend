#!/usr/bin/env python3
"""
Defines the class LFUCache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Defines an LRU caching system
    """
    def __init__(self):
        """
        Initializes cache with a dict and order list of tuples to
        keep track of the usage of items.
        """
        super().__init__()
        # list of tuples with order and frequency of usage
        self.order = []

    def put(self, key, item):
        """
        Add item to cache.
        """
        if key is not None and item is not None:
            cache_len = len(self.cache_data)
            max_items = BaseCaching.MAX_ITEMS
            if cache_len >= max_items and key not in self.cache_data:
                discard = self.to_discard()
                print('DISCARD: {}'.format(discard[0]))
                del self.cache_data[discard[0]]
                self.order.remove(discard)
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
        times = 1
        for tup in self.order:
            k, t = tup
            if key == k:
                times += t
                self.order.remove(tup)
                break
        self.order.append((key, times))

    def to_discard(self):
        """
        Determines which item to discard based on least frequently
        used and then least recently used
        """
        i = 0
        discard = self.order[i]
        for tup in self.order:
            if tup[1] < discard[1]:
                discard = self.order[i]
            i += 1
        return discard
