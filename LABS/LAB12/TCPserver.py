#!/usr/bin/env python

import socket

# socket.AF_INET is the internet address familiy for IPv4
# socket.STOCK_STREAM is the sicket type for TCP - which is the protocol that will be used to transport messages
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind() assigns an IP address and prt number to a socket instance.
# Assign an IP address here corresponding to your adapter (check with ipconfig in your host terminal)
# Port numver 0 to 1023 are reserved for common TCP/IP applications and are what we call well-known ports.
s.bind(('10.0.0.59', 2345))

# Listen() is used below to mark our socket instances as a passice socket - a socket that will be used
# to accept incoming connection requests with accept() method.
# You can pass inn a number to this method to specify a maximum lenght of a queue of pending
# connections.
# Example: If you call serverSocket.listen(2) and 3 connection requests come in before you
# call accept(), then 1 will be dropped.
s.listen(1)

while True:
    print("Listening for connections...")
    data, source = s.accept()
    print("Connection with", source,  " established!")

    # Recives a coded message
    msg_send = "Hello! You are connected to the server!".encode('utf-8')
    data.send(msg_send)
    while True:
        some_msg= data.recv(1024).decode('utf-8')
        print("Message from Client: " + some_msg)

        if some_msg == "Bye":
            break

        response_message = input("Write something to the client: ")
        msg_send = response_message.encode('utf-8')
        data.send(msg_send)
        print("Client is responding ...")

    msg_send = "Bye received, connection ended.".encode('utf-8')
    data.send(msg_send)
    data.close()
    break
    # final break can be removed if we want the server to keep listening for other connections
