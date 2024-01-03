#!/usr/bin/python3
""" Creates class BasicCache that inherits from BaseCaching """


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines BaseCache """
    def put(self, key, item):
        """
        Add an item in the cache.
        Args:
            key: Key to identify the item.
            item: Item to be stored in the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        Args:
            Key: key to retrieve the item from the cache.
        Returns:
        The item associated with the key, or None if not found.
        """
        return self.cache_data.get(key)
