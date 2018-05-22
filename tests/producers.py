# -*- coding: utf-8 -*-
"""
@author: v.villar


Test how much message are we able to process
"""

import socket

import time

s = socket.socket()
host = '127.0.0.1'  # needs to be in quote
port = 4321
s.connect((host, port))
print(str(s.recv(1024)))

start_time = time.time()
print("Start time: ", start_time)
for i in range(0, 25000):
    s.send("Sending new message\n".encode())
    s.recv(1024)
    # print("the message has been sent")
elapsed_time = int(time.time() - start_time)
print("Time elapsed: ",
      '{:02d}:{:02d}:{:02d}'.format(elapsed_time // 3600, (elapsed_time % 3600 // 60), elapsed_time % 60))
r = input("")
