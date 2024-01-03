#!/usr/bin/python3
""" Creates class LIFOCache that inherits from BaseCaching """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Defines BaseCache """

    def __init__(self):
        """ Initialize LIFOCache """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        Args:
            key: Key to identify the item.
            item: Item to be stored in the cache.
        """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
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
