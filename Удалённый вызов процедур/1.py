import socket

host = "127.0.0.32"
port = 12345

client = socket.socket()

client.connect((host, port))

client.send('Hello world!'.encode())

client.close()