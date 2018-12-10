# -*- coding: utf-8 -*-
import socket, logging 
from thread import start_new_thread
from threading import Thread
from util import *
from random import choice
import json
import select
import sys

class MiddleWare(object):
	"""docstring for Middleware"""
	def __init__(self, proxy_list, host):
		self.port = 54321
		self.host = host
		self.buffer_size = 8192*8
		self.read_list = []
		self.proxy_list = proxy_list
		self.sock_port = None

	def sendRequestToProxy(self, data, conn):	
		if not self.proxy_list:
			print "Nenhum serviço conectado"
			conn.close()
			self.read_list.remove(conn)
			return
		
		proxy_tuple = choice(self.proxy_list)
		try:
	
			print "\nProxy escolhido \nPorta: {}\tHost: {}\n".format(proxy_tuple['port'], proxy_tuple['host'])
			self.ACK_message()
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((proxy_tuple['host'], proxy_tuple['port']))
			self.ACK_message() #ACK
			sock.send(data)
			response = sock.recv(self.buffer_size)
			self.ACK_message() #ACK
			conn.send(response)
			conn.close()
			self.read_list.remove(conn)
			sock.close()
			
		except Exception as e:
			if self.proxy_list == []:
				conn.send(response)
				sock.close()
				self.read_list.remove(conn)
				conn.close()
				sys.exit(0)

			elif proxy_tuple in self.proxy_list:
				self.proxy_list.remove(proxy_tuple)
				print "\nServidor proxy {} removido:\nNova lista: {}\n".format(proxy_tuple, self.proxy_list)
				self.ACK_message(0x1, proxy_tuple) #ACK

			proxy_tuple = choice(self.proxy_list)
			print "\nProxy escolhido \nPorta: {}\tHost: {}\n".format(proxy_tuple['port'], proxy_tuple['host'])
			self.ACK_message()
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((proxy_tuple['host'], proxy_tuple['port']))
			self.ACK_message() #ACK
			sock.send(data)
			response = sock.recv(self.buffer_size)
			self.ACK_message() #ACK
			conn.send(response)
			sock.close()
			self.read_list.remove(conn)
			conn.close()
			print e
			return
		
	def removeL(self, val):		
		if val in self.proxy_list:
			self.proxy_list.remove(val)
			print "Dados removidos da list: {}".format(self.proxy_list)
			return True
		else:
			print "Lista permanece a mesma: {}".format(self.proxy_list)
			return False

	def ACK_message(self, bitVerify = 0x0, removedProxy = {}):
		try:
			connection, address = self.sock_port.accept()
			recv_data = json.loads(connection.recv(self.buffer_size))
			proxy_tuple = recv_data['tupla']

			if recv_data['status'] == 'up':
				if recv_data['update'] == 0x1:
					print "\nProxy {} comunicou perda de conexão com algum membro do cluster".format(address)
					for i in self.proxy_list:
						if i not in proxy_tuple['port']:
							if self.proxy_list:
								self.proxy_list.remove(i)
							else:
								print "\nNenhum serviço conectado.\nEstado atual do MiddleWare: {}\n".format(self.proxy_list)

					print "Novo cluster: {}\n".format(self.proxy_list)
				
				for i in proxy_tuple['port']:
					if i not in self.proxy_list and i != removedProxy:
						print "Nova conexão: ({},{})".format(i['host'], i['port'])
						self.proxy_list.append(i)

				msg = {'update': bitVerify, 'list': self.proxy_list}
				connection.send(json.dumps(msg))

			if recv_data['status'] == 'down':
				if self.removeL(recv_data['port']):
					print "Nó ({},{}) saiu.\nNova lista de conexões: {} ".format(proxy_tuple['host'], proxy_tuple['port'], self.proxy_list) 
		
		except Exception as e:
			if e is ValueError:
				pass
			else:
				raise e
			return
	
	def loopACK(self):
		while True:
			self.ACK_message()

	def start(self):
		try:

			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind(("localhost", self.port))
			sock.listen(10)
			self.sock_port = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock_port.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.sock_port.bind(("localhost", self.port + 1))
			self.sock_port.listen(10)

		except Exception, e:
			print "Erro ao iniciar o servidor Middleware"
			print e
			sock.close()
			return

		self.read_list = [sock]
		while True:
			
			start_new_thread(self.loopACK, ())
	
			readable, writable, errored = select.select(self.read_list, [], [])
			for s in readable:
				if s is sock:
					conn, addr = sock.accept()
					self.read_list.append(conn)
				else:
					data = s.recv(self.buffer_size)
					start_new_thread(self.sendRequestToProxy, (data, s))	
					
