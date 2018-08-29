import socket
import os
import sys
import select
from threading import Thread

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
	print "Numero de argumentos invalido"
	print "Esperado:\tpython script.py 'IP' 'PORT'"
	exit()
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
cliente.connect((IP , PORT))

def enviar():
	'''Funcao de envio de dados '''
	while True:
		mensagem =  sys.stdin.readline()
		cliente.send(mensagem)
		sys.stdout.write("[Voce] ")
		sys.stdout.write(mensagem)
		sys.stdout.flush()

def receber():
	'''Funcao de recebimento de dados '''
	while True:
		mensagem = cliente.recv(1024)
		print mensagem

''' Thread para envio de dados '''
thread1 = Thread(target=enviar)
''' Thread para receber dados '''
thread2 = Thread(target=receber)

thread1.start()
thread2.start()

