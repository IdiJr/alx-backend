#!/usr/bin/python3
""" Creates class FIFOCache that inherits from BaseCaching """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Defines BaseCache """

    def __init__(self):
        """ Initialize FIFOCache """
        self.queue = []
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
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item
            if len(self.queue) > self.MAX_ITEMS:
                delete = self.queue.pop(0)
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
        return self.cache_data.get(key)
