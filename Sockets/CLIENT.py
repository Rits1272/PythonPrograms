import socket 
import sys
import select

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To avoid port problem

IP_ADD = '192.168.43.48'
PORT = 1234

client.connect((IP_ADD, PORT))

while True:
	sockets_list = [sys.stdin, client]
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets:
		if socks == client:
			message = socks.recv(1024)
			print(str(message))
		
		else:
			message = sys.stdin.readline()
			client.send(message.encode('utf-8'))
			sys.stdout.write("<You>")
			sys.stdout.write(message)
			sys.stdout.flush()

client.close()