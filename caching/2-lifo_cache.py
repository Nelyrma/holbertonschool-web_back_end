#!/usr/bin/python3
"""LIFOCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a cache system
    """

    def __init__(self):
        """initialize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        add an item in the cache using LIFO algorithm
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-1)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        returns the value in the dictionary linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
