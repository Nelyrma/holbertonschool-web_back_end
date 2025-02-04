#!/usr/bin/python3
"""
BasicCache module
"""

BaseCaching = __import__('base_caching.').BaseCaching

class BasicCache(BaseCaching):
    """
    inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """assign to the self.cache_data dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        
        return self.cache_data[key]