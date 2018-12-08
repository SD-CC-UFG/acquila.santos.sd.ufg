# -*- coding: utf-8 -*-
import socket, logging 
from thread import start_new_thread
from threading import Thread
from util import *
from random import choice
import json
import signal
import sys
import select

class MiddleWare(object):
	"""docstring for Middleware"""
	def __init__(self, proxy_list):
		self.port = 54321
		self.buffer_size = 8192*8
		self.read_list = []
		self.proxy_list = proxy_list
		self.sock_port = None


	def status503(self, conn):
		string = "HTTP/1.1 503 Service Unavailable"
		string += "Content-Type: text/html; charset=UTF-8"
		string += "Content-Encoding: gzip"
		string += "Vary: Accept-Encoding"
		string += "Date: Wed, 28 Nov 2018 14:55:04 GMT"
		string += "Server: LiteSpeed"
		string += "Access-Control-Allow-Methods: GET"
		string += "Connection: close"
		conn.send(string)

	def sendRequestToProxy(self, data, conn):	
		if not self.proxy_list:
			print "Nenhum serviço conectado"
			conn.close()
			self.read_list.remove(conn)
			return
		
		i = choice(self.proxy_list)
		try:
			
			print "Proxy escolhido na porta: {}\n".format(i)
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(("localhost", i))
			sock.send(data)
			response = sock.recv(self.buffer_size)
			conn.send(response)
			conn.close()
			self.read_list.remove(conn)

			sock.close()
		except:
			self.proxy_list.remove(i)

	def getPort(self):
		try:
			connection, address = self.sock_port.accept()
			recv_data = json.loads(connection.recv(self.buffer_size))
			
			if recv_data['middlewareOff']:
				print "Servidor caiu...\nReiniciar lista de peers {}".format(recv_data['middlewareOff'])
				for i in recv_data['port']:
					if i not in self.proxy_list:
						self.proxy_list.append(i)

				connection.send(json.dumps(self.proxy_list))
				print "{} enviou uma lista de peers: {}".format(address, self.proxy_list)

			else:
				if recv_data['status'] == 'up':
					if not (recv_data['port'] in self.proxy_list):
						# try:
						self.proxy_list.append(int(recv_data['port']))
						# except Exception as e:
						# 	raise e
						print "Nova conexão: {}".format(recv_data['port'])

					print "ACK de verificação recebido de {}: {}".format(address, self.proxy_list)
					connection.send(json.dumps(self.proxy_list))

				elif recv_data['status'] == 0:
					if self.proxy_list:
						self.proxy_list.remove(recv_data['port'])
						print "Nó {} saiu.\nNova lista de conexões: {} ".format(recv_data['port'], self.proxy_list) 

		except Exception as e:
			if e is ValueError:
				pass
			else:
				raise e

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
		#print self.proxy_list
		self.read_list = [sock]
		while True:
			
			start_new_thread(self.getPort,())

			
			conn, addr = sock.accept()
					
				
			data = conn.recv(self.buffer_size)
			start_new_thread(self.sendRequestToProxy, (data, conn))	
					