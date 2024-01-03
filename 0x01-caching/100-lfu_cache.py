#!/usr/bin/python3
""" Creates class LFUCache that inherits from BaseCaching """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ Defines LFUCache """

    def __init__(self):
        """ Initialize LFUCache """
        self.queue = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache.
        Args:
            key: Key to identify the item.
            item: Item to be stored in the cache.
        """
        if key and item:
            if (len(self.queue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                delete = self.queue.pop(0)
                self.lfu.pop(delete)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu[key] += 1
            else:
                self.lfu[key] = 0

            insert_index = 0
            while (insert_index < len(self.queue) and
                   not self.lfu[self.queue[insert_index]]):
                insert_index += 1
            self.queue.insert(insert_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        Args:
            Key: key to retrieve the item from the cache.
        Returns:
        The item associated with the key, or None if not found.
        """
        if self.cache_data.get(key):
            self.lfu[key] += 1
            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.lfu[key] >=
                       self.lfu[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key)
