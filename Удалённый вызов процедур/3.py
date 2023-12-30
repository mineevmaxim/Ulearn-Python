import socket
import threading

import pandas as pd


def answer(client, df):
    while True:
        message = client.recv(1024).decode()
        website = df[df['Name'] == message]['Website'].values[0]
        client.send(website.encode())


def start_server():
    df = pd.read_csv('organizations.csv')
    host = "127.0.0.32"
    port = 12345
    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=answer(client, df)).start()
