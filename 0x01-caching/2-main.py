#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.order)
my_cache.put("E", "Battery")
print(my_cache.order)
my_cache.print_cache()
my_cache.put("C", "Street")
print(my_cache.order)
my_cache.print_cache()
my_cache.put("F", "Mission")
print(my_cache.order)
my_cache.print_cache()
my_cache.put("h", "San Francisco")
print(my_cache.order)
my_cache.put("I", "San Francisco")
print(my_cache.order)
my_cache.put("J", "San Francisco")
print(my_cache.order)
my_cache.put("K", "San Francisco")
print(my_cache.order)

