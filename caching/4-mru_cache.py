#!/usr/bin/python3
"""MRUCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a cache system
    """

    def __init__(self):
        """initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """add an item using MRU"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop(-1)
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

    def get(self, key):
        """
        returns the value in the dictionary
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
