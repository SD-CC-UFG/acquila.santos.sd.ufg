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



	def sendRequestToProxy(self, data, conn):	
		if not self.proxy_list:
			return
		i = choice(self.proxy_list)
		try:
			
			print i
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
			if recv_data['status'] == 'up':
				if not (recv_data['port'] in self.proxy_list):
					self.proxy_list.append(int(recv_data['port']))
					print "Nova conexão: {}".format(recv_data['port'])
				print self.proxy_list
				connection.send(json.dumps(self.proxy_list))
			elif recv_data['status'] == 'shutdown':
				self.proxy_list.remove(recv_data['port'])
				print "Nó {} saiu.\nNova lista de conexões: {} ".format(recv_data['port'], self.proxy_list) 
			
		except Exception as e:
			raise e
			pass

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
			print "Erro ao iniciar o servidor Proxy"
			print e
			sock.close()
			return
		#print self.proxy_list
		self.read_list = [sock]
		while True:
			
			start_new_thread(self.getPort, ())

			readable, writable, errored = select.select(self.read_list, [], [])
			
			for s in readable:
				if s is sock:
					conn, addr = sock.accept()
					self.read_list.append(conn)
				else:
					data = s.recv(self.buffer_size)
					start_new_thread(self.sendRequestToProxy, (data, s))	
					