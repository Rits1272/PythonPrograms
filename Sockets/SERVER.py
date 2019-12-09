import socket
from _thread import * 
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reconnect

IP_ADD = '192.168.43.48'
PORT = 1234

server.bind((IP_ADD, PORT))
server.listen(5)

list_of_clients = []

def clientThread(conn, addr):
    conn.send("Welcome to the LAN chat".encode('utf-8'))

    while True:
        message = conn.recv(1024)
        if message.decode('utf-8'):
            sys.stdout.write(addr[0] + ">" + message.decode('utf-8'))

            message_to_send = (addr[0] + "> " + str(message)).encode('utf-8')
            broadcast(message_to_send, conn)
      

def broadcast(msg, connection):
    for client in list_of_clients:
        if client != connection:
            client.sendall(msg)
        

def remove(conn):
    if conn in list_of_clients:
        list_of_clients.remove(conn)

print('<Listening to clients>')
while True:
    conn, addr = server.accept()

    list_of_clients.append(conn)

    print(addr[0] + " connected!")
    start_new_thread(clientThread, (conn, addr,)) # from _thread class

conn.close()
server.close()

