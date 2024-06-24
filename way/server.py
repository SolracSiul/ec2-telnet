import socket
import os


ADDR = "10.0.1.147"
PORT = "3000"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ADDR, int(PORT)))
server_socket.listen()


connection, address = server_socket.accept()

while True:
    buffer = connection.recv(64)
    print(buffer)
    if len(buffer) >= 10:
        break
connection.close()

