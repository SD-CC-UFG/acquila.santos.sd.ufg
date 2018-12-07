# -*- coding: utf-8 -*-
import socket, logging 
from thread import start_new_thread
from threading import Thread
from util import *
from random import randint
import signal
import sys

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Thread.join(self)
        return self._return

class MiddleWare(object):
	"""docstring for Middleware"""
	def __init__(self, num_proxy):
		self.port = 54321
		self.buffer_size = 8192*8
		self.proxy_list = []
		self. num_proxy = num_proxy

	def connectProxy(self, p = 4321):
		sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(self.num_proxy)]
		for sock in sockets:
			try:
				sock.connect(("localhost", p))
			except Exception as e:
				print "Erro ao conectar no proxy"
				raise e
				sock.close()
				return
			p = p + 1
			self.proxy_list.append(sock)

	def closeAll(self):
		for sock in self.proxy_list:
			sock.close()
			self.proxy_list.remove(sock)

	def sendRequestToProxy(self, data, conn):	
		#sock = 0
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(("localhost", 4321))
		#i = randint(0, len(self.proxy_list) - 1)
		#print ("Dados enviados para o proxy %d: \n%s" % (i,data))
		#sock = self.proxy_list[i]
		sock.send(data)
		#sys.stdout.flush()
		#self.proxy_list.remove(sock)
		response = sock.recv(self.buffer_size)
		#self.closeAll()
		#print response
		conn.send(response)
		conn.close()

		sock.close()
		
	def start(self):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind(("localhost", self.port))
			sock.listen(10)
		except Exception, e:
			print "Erro ao iniciar o servidor Proxy"
			print e
			sock.close()
			return
		#print self.proxy_list

		while True:
				
			conn, addr = sock.accept()
			data = conn.recv(self.buffer_size)
			start_new_thread(self.sendRequestToProxy, (data, conn))	