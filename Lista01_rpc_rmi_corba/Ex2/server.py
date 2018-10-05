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
				sexo = msg[1]
				idade = int(msg[2])

				msgEnv1 = 'Maioridade'
				msgEnv2 = 'Não atingiu a maioridade'

				
				if (sexo == 'masculino' and idade >= 18) or (sexo == 'feminino' and idade >= 21):
					msgEnv = msg[0] + ': ' + msgEnv1
					conexao.send(msgEnv)

				elif (sexo == 'masculino' and idade < 18) or (sexo == 'feminino' and idade < 21):
					msgEnv = msg[0] + ': ' + msgEnv2
					conexao.send(msgEnv)

		except:
			pass


		

while True:

	conexao, endereco = server.accept()
	
	print endereco[0] + " conectou!"

	clientes.append(conexao)

	start_new_thread(newClient, (conexao, endereco))

conexao.close()
server.close()




