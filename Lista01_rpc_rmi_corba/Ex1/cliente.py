import socket
import os
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
	print "Numero de argumentos invalido"
	print "Esperado:\tpython script.py 'IP' 'PORT'"
	exit()
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
server.connect((IP , PORT))


while True:

	sockets = [sys.stdin , server]
	
	l_socket, gravar_socket, erro_socket = select.select(sockets,[],[])

	for s in l_socket:
		if s == server:
			mensagem = s.recv(1024)
			print mensagem
			if mensagem != 'Bem vindo ao servico!':
				exit(0)
		else:
			nome =  raw_input()
			cargo =  raw_input()
			salario =  raw_input()

			msg = nome + ':' + cargo + ':' + salario
			server.send(msg)


server.close()