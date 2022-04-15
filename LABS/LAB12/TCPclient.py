#!/usr/bin/env python

import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP socket for IPv4

c.connect(('localhost', 2345))

msg = c.recv(1024).decode('utf-8')
print(msg)

some_msg = "someString"
while some_msg != "Bye":
    some_msg = input("Write something to server (or Bye to end connection): ")  # sending option to client to write something

    print("Server is responding: ")
    msg_send = some_msg.encode('utf-8')
    c.send(msg_send)

    msg_receive = c.recv(1024).decode('utf-8')
    print("Message from Server: " + msg_receive)

# Recive message - recv(1024) indicates that 1024 bytes bytes will be read at most
msg_receive = c.recv(1024).decode('utf-8')
print(msg_receive)  # connection has ended

