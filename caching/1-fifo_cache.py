#!/usr/bin/python3
"""FIFOCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        add an item using FIFO"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        returns the value in the dictionary linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
