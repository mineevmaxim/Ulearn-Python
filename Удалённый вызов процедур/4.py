import socket
import json
import pandas as pd
import threading


def get_website(df, name):
    return df[df['Name'] == name]['Website'].values[0]


def get_country(df, name):
    return df[df['Name'] == name]['Country'].values[0]


def get_number_of_employees(df, name):
    return df[df['Name'] == name]['Number of employees'].values[0]


def answer(client, df):
    while True:
        message = client.recv(1024).decode()

        if message == 'exit':
            client.close()
            break

        if len(message) == 0:
            break

        message = json.loads(message)

        if message['operation'] == 'get_website':
            client.send(('{"result": "' + get_website(df, message['name']) + '"}').encode())

        if message['operation'] == 'get_country':
            client.send(('{"result": "' + get_country(df, message['name']) + '"}').encode())

        if message['operation'] == 'get_number_of_employees':
            client.send(('{"result": "' + str(get_number_of_employees(df, message['name'])) + '"}').encode())


def start_server():
    df = pd.read_csv("organizations.csv")
    host = "127.0.0.32"
    port = 12345

    server = socket.socket()
    server.bind((host, port))
    server.listen(5)

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=answer(client, df)).start()


start_server()