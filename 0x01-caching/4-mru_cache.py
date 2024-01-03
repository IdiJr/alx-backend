#!/usr/bin/python3
""" Creates class MRUCache that inherits from BaseCaching """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Defines MRUCache """

    def __init__(self):
        """ Initialize MRUCache """
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
            self.stack.append(key)
            self.cache_data[key] = item
            if len(self.stack) > self.MAX_ITEMS:
                delete = self.stack.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """
        Get an item by key
        Args:
            Key: key to retrieve the item from the cache.
        Returns:
        The item associated with the key, or None if not found.
        """
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
