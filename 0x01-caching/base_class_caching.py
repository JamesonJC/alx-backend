#!/usr/bin/python3
"""
Base class with given methods for caching
"""

class BaseCaching:
    """
    BaseCaching stores data in a a dictionary
    for your system to retrieve the dat much quiker
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialization of variable
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Disolaying the cache
        """

        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, items):
        """
        Puting items in the cache dictionary
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        Access Items with their keys
        """
        raise NotImplementedError("get must be implemented in your cache class")
