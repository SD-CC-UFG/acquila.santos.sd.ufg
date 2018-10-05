import socket
import os
import sys
from thread import *
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
	print "Numero de argumentos invalido"
	print "Esperado:\tpython script.py 'IP' 'PORT'"
	exit()

IP = str(sys.argv[1])
PORT = int(sys.argv[2])

server.bind((IP , PORT))
server.listen(100)

clientes = []

def newClient(conexao, endereco):
	conexao.send("Bem vindo ao servico!")

	while True:
		''' O valor de retorno eh uma string com o conteudo informado '''
		try:
			msg = conexao.recv(1024)
			if msg != '':

				msg = msg.split(':')
				print msg
				n1 = float(msg[0])
				n2 = float(msg[1])
				n3 = float(msg[2])
				
				msgEnv1 = 'APROVADO'
				msgEnv2 = 'REPROVADO'
				m1 = (n1 + n2)/2

				if m1 >= 7.0 :
					conexao.send(msgEnv1)

				elif m1 > 3.0 and m1 < 7.0:
					m2 = (m1 + n3)/2

					if m2 > 5.0:
						conexao.send(msgEnv1)
					else:
						conexao.send(msgEnv2)
				else:
					conexao.send(msgEnv2)



		except:
			pass


		

while True:

	conexao, endereco = server.accept()
	
	print endereco[0] + " conectou!"

	clientes.append(conexao)

	start_new_thread(newClient, (conexao, endereco))

conexao.close()
server.close()




