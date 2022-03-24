#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    message = b''  # empty bracker for message(quote) to be storeeed
    addr = ("23.28.179.206", 17)   # specifyinh address ad port

    s.sendto(message, addr) # sending data over to the address

    data, address = s.recvfrom(1024)    # receiving the data from the address
    print(data.decode())
