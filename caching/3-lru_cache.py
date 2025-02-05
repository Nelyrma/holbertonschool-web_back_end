#!/usr/bin/python3
"""LRUCache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        add an item using LRU algorithm"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        if key in self.order:
            self.order.remove(key)  # prevents duplicate keys

        # put the key to the most recently used position
        self.order.append(key)

    def get(self, key):
        """
        returns the value in the dictionary linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        if key in self.order:
            self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
