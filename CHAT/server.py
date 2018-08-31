import socket
import os
import sys
from threadPool import ThreadPool

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

''' Funcao de broadcast:  Envia a mensagem para todo os clientes constados no servidor '''
def broadcast(mensagem, conexao):
	for i in clientes:
		''' Evitar que o cliente mande uma mensagem para si mesmo '''
		if i != conexao:
			try:
				i.send(str(mensagem))
			except:
				''' Caso ocorra algum erro fechar comunicacao '''
				i.close()
				
				''' Remover cliente da lista
					Interrompendo sua conexao'''

				if i in clientes:
					clientes.remove(i)

def clientThreadMain():
	''' Cria-se 20 threads pre-alocadas'''
	thread = ThreadPool(20)
	''' Laco principal do servidor '''
	while True:

		conexao, endereco = server.accept()
	
		print endereco[0] + " conectou!"

		''' Quando um cliente se conecta, eh adicionado a uma lista de clientes (usado para o broadcast) '''
		clientes.append(conexao)
		thread.insert_job(newClient, conexao, endereco)


def newClient(conexao, endereco):
	conexao.send("Bem vindo ao chat!")

	while True:
		''' O valor de retorno eh uma string com o conteudo informado '''
		
		mensagem = conexao.recv(1024)

		''' Impedir de ser enviadas mensagens vazias 
			Aqui ele recebe mensagens '''

		if mensagem:

			print "[" + endereco[0] + "] " + mensagem

			''' Enviar mensagem ao cliente '''

			mensagemEnvio = "[" + endereco[0] + "] " + mensagem

			''' Enviar mensagem para outros clientes '''
			broadcast(mensagemEnvio, conexao)

		else:

			''' Se existir esta conexao na lista de clientes '''
			
			if conexao in clientes:
				clientes.remove(conexao)

		''' No terminal do servidor aparecera as mensagens inseridas '''
	

clientThreadMain()

conexao.close()
server.close()




