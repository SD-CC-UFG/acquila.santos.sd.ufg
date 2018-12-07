# -*- coding: utf-8 -*-
import socket, logging 
from thread import start_new_thread
from cache import Cache
from util import *

# Configurar o logging

logging.basicConfig(filename = 'proxy.log', filemode='a',format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

log = logging.getLogger('proxy')

class ServidorProxy():
	"""docstring for ServidorProxy"""
	def __init__(self, port):
		self.port = port
		self.buffer_size = 8192*10
		self.conexoes = 10
		self.cacheSize = 9999999
		self.cache = Cache(self.cacheSize)
		self.host = "localhost"
		print "|****************************************|"
		print"|\tHTTP Proxy Server\t\t |\n|\tPort: %d\t\t\t |\n|\tCache Size: %ld\t\t |\n|\tHost: %s\t\t\t |" % (self.port, self.cacheSize, self.host)  
		print "|****************************************|"

	def start(self):
		
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind((self.host, self.port))
			sock.listen(self.conexoes)
		except Exception, e:
			print "Erro ao iniciar o servidor Proxy"
			sock.close()
			print e
			return
		# Primeiro devo inciar uma conexão com o middleware. O erro estava acontecendo quando colocava no laço, pois o processo
		#   travava esperando por uma conexão
		
		while True:
			try:
				conn, addr = sock.accept()
				data = conn.recv(self.buffer_size)
			except Exception as e:
				print "Proxy encerrado"
				raise e
				return
		
			start_new_thread(self.requestHandler, (data, conn, addr))
			

	def handleExistingUrl(self, url, host, data, recv_data, conn):
		
		log.info("Cache HIT: " + url)
		response = self.cache.getData(url)
		conn.send(response)
		conn.close()

	def handleNotExistindgUrl(self, url, host, data, recv_data, conn):
		log.info("Cache MISS: "+ url)
	
		response = getHttp(host, data, self.buffer_size)
		self.cache.cachePush(url, response)

		conn.send(response)
		conn.close()

	def requestHandler(self, data, conn, addr):

		#Fazer o parsing da requisicao do cliente, que retorna um dicionario de dados chave-valor
		recv_data = parseHeader(data)
		if recv_data['method'] != 'GET':
			notImplementedMethod(conn)
			return
		# Recuperar url e hpst do servidor requisitado pelo cliente
		url = recv_data['url']
		host = recv_data['Host']
		log.info("Requisicao de %s para %s" % (addr, url))

		# Caso o campo 'no-cache' do cabecalho esteja evidente em 'pragma' ou 'cache-control', nao armazenar em cache
		if self.cache.existingUrl(url):
			self.handleExistingUrl(url, host, data, recv_data, conn)
		else:
			self.handleNotExistindgUrl(url, host, data, recv_data, conn)


