#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()       


print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(0, 10)
print(res)

del server._Server__indexed_dataset[3]
del server._Server__indexed_dataset[6]
del server._Server__indexed_dataset[7]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(0, 10))

# # 5- request again initial next index -> same data page as the request 2-
# print(server.get_hyper_index(res.get('next_index'), page_size))
