import socket

PORT = 8000
SERVER = "127.0.0.1"
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
	client.send(msg)
	
send(b'Hello\r\n' )