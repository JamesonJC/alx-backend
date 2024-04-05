#!/usr/bin/env python3
"""
BaseCaching module
"""

from typing import Dict, Any, Optional
from base_class_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Child calss of BaseCaching, also stores data in dictionary
    """
    """def __init__(self):
        
        Calls The parent class supe:
        
        super().__init__()
    """

    def put(self, key: Any, item: Any) -> None:
        """
        Adding data for adding data to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieving the cache
        """
        return self.cache_data.get(key, None)

if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Elon")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D")) # D return None
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
