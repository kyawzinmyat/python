import socket



		


def start():
	PORT = 8000
	SERVER = socket.gethostbyname(socket.gethostname())

	ADDR=(SERVER,PORT)

	server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



	server.bind(ADDR)

	server.listen(1)
	print(f"Server is listening on {SERVER}")

	conn,addr=server.accept()
	msg = conn.recv(1025)
	print(f"[{addr}] {msg}")
	server.close()

	
start()
	
