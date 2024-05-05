#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(0, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(2158, 9))
print("---")
print(server.get_hyper(1, 100))
