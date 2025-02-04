#!/usr/bin/python3
""" BasicCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """Assigns to the dictionary self.cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]