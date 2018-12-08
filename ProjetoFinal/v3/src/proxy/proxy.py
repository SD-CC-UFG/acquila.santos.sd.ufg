# -*- coding: utf-8 -*-
import socket, logging, select
from thread import start_new_thread
from cache import Cache
from util import *
import json
import time
#from p2p import send, receive
import socket
try:
		import cPickle as pickle
except ImportError:
		import pickle
import hmac
import hashlib

SEND_RECEIVE_CONF= lambda x:x
SEND_RECEIVE_CONF.key="ctv4eys984cavpavt5snldbkrw3"
SEND_RECEIVE_CONF.last_recipient="localhost"
SEND_RECEIVE_CONF.last_port= 23208
SEND_RECEIVE_CONF.hashfunction= hashlib.sha1
SEND_RECEIVE_CONF.hashsize= 160 / 8 #sha1 has 160 bits
SEND_RECEIVE_CONF.magic= 'sendreceive'
SEND_RECEIVE_CONF.buffer= 8192

# Configurar o logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class ServidorProxy():
	"""docstring for ServidorProxy"""
	def __init__(self, port = 4321):
		self.port = port
		self.buffer_size = 8192*10
		self.conexoes = 10
		self.cacheSize = 9999999
		self.cache = Cache(self.cacheSize)
		self.host = "localhost"
		self.peerList = []
		self.p2pSocket = None
		print "|****************************************|"
		print"|\tHTTP Proxy Server\t\t |\n|\tPort: %d\t\t\t |\n|\tCache Size: %ld\t\t |\n|\tHost: %s\t\t\t |" % (self.port, self.cacheSize, self.host)  
		print "|****************************************|"
		
	def sendVerificationMessage(self, middlewareOff, port):
		alertS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		alertS.connect(("localhost", 54322))
		# A mensagem de controle para o proxy pode ser avisando que o middleware esteve off, ou somente um ACK comum
		msg = {'middlewareOff': middlewareOff, 'status': 'up', 'port': port}
		alertS.send(json.dumps(msg))
		peerResponse = json.loads(alertS.recv(self.buffer_size))
		print "[Middleware] ACK de resposta do middleware: {}".format(peerResponse)
		return peerResponse

	def controlMessage(self):
		
		try:
			peerResponse =  self.sendVerificationMessage(False, self.port)
			self.peerList = peerResponse
		except Exception as e:
			print "Middleware rejeitando conexoes"
			peerResponse = None
			cont = 0
			while peerResponse is None or cont < 100:
				try:
					if not self.port in self.peerList:
						self.peerList.append(self.port)
					peerResponse =  self.sendVerificationMessage(True, self.peerList)
					self.p2pSend()
					return
				except socket.error as e:
					cont += 1
					print("Conexão Falhou: {}").format(e)
					print("Tentativa {} of 100").format(cont)
					time.sleep(5)

	def loopControl(self):
		try:
			while True:
				self.controlMessage()
		except KeyboardInterrupt as e:
			alertS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			alertS.connect(("localhost", 54322))
			msg = {'middlewareOff': False, 'status': 'shutdown', 'port': self.port}
			alertS.send(json.dumps(msg))
			raise e
			
	def loopReceive(self):
		while True:
			self.p2pReceive()
		
	def start(self):
	
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind((self.host, self.port))
			sock.listen(self.conexoes)
		

			self.p2pSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.p2pSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.p2pSocket.bind(("localhost", self.port*2))
			self.p2pSocket.listen(3)
			
		except Exception, e:
			print "Erro ao iniciar o servidor Proxy"
			sock.close()
			print e
			return
		
		try:
			while True:
				
				start_new_thread(self.loopReceive, ())
				start_new_thread(self.loopControl, ())
				try:
					conn, addr = sock.accept()

				except Exception as e:
					print "Proxy encerrado"
					raise e
					return
			
				data = conn.recv(self.buffer_size)
				start_new_thread(self.requestHandler, (data, conn, addr))

		except KeyboardInterrupt as e:
			alertS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			alertS.connect(("localhost", 54322))
			msg = {'middlewareOff': False, 'status': 'shutdown', 'port': self.port}
			alertS.send(json.dumps(msg))
			raise e
			
			
	def p2pSend(self):
		ports_bootstrap = [4321*2, 4322*2]
		for i in self.peerList:
			if i*2 != self.port*2:
				try:
					msg = {'cache': self.cache, 'peerList': self.peerList}
					self.send(msg, "localhost", i*2)
					pass
				except Exception as e:
					raise e
					break

	def p2pReceive(self):

		try:
			recv_cache = self.receive()
			if not recv_cache:
				return
		except Exception as e:
			print "[P2P] Dados recebidos via conexão P2P corrompidos"
		
		#Recuperar as url's do cache reccebido
		urlInRecvCache = recv_cache.returnKeys()
		
		#Verificar se as url estão presentes no cache local
		#caso estiver ignorar, caso contrário inserir no cache
		for url in urlInRecvCache:
			if not self.cache.existingUrl(url):
				response = recv_cache.getData(url)
				self.cache.cachePush(url, response)
				print "\n[P2P] Objeto %s adicionado ao cache\n" % (url)
			else:
				print "\n[P2P] Objeto %s já está atualizado\n"%(url)
			
	def send(self, obj, host = None, port = None):

		global SEND_RECEIVE_CONF
		SRC = SEND_RECEIVE_CONF
		SRC.last_recipient= host
		SRC.last_port= port
		connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connection.connect( (host, port) )	
		serialized= pickle.dumps( obj )
		signature= hmac.new( SRC.key, serialized,  SRC.hashfunction).digest()
		assert len(signature)==SRC.hashsize
		message= SRC.magic + signature + serialized
		connection.send( message )
		response= connection.recv( SRC.buffer )
		if response!=SRC.magic:
			raise Exception("Ack para comunicação corrompido")
		connection.close()

	def receive(self):
		global SEND_RECEIVE_CONF
		SRC = SEND_RECEIVE_CONF

		try:
			conn, addr = self.p2pSocket.accept()
			print '[P2P] Conexão com {}'.format(addr)
		except socket.error as e:
			self.p2pSocket.close()
			raise e
		data = conn.recv( SRC.buffer )
		if len(data) < len( SEND_RECEIVE_CONF.magic)+SEND_RECEIVE_CONF.hashsize:
			raise Exception("Mensagem recebida é muito pequena")
		if not data.startswith( SRC.magic ):
			conn.close()
			self.p2pSocket.close()
			raise Exception("Ack para comunicação corrompido. Não é uma comunicação P2P")
		i1= len(SRC.magic)
		i2= i1+SRC.hashsize
		signature= data[i1:i2]
		message= data[i2:]
		good_signature= hmac.new( SRC.key, message,  SRC.hashfunction).digest()
		if signature!=good_signature:
			conn.close()
			self.p2pSocket.close()
			raise Exception("Assinaturas erradas")
		conn.send( SRC.magic )
		conn.close()
		obj= pickle.loads(message)
		antes = self.peerList 
		for i in obj['peerList']:
			if i not in self.peerList:
				self.peerList.append(i)
				print '[P2P] lista de proxies atualizados\n\t Antes: {}\n\t Depois: {}'.format(antes, self.peerList)

		print '[P2P] {} enviou seu cache'.format(addr)
		return obj['cache']


	def handleExistingUrl(self, url, host, data, recv_data, conn):
		
		logging.info("Cache HIT: " + url)
		response = self.cache.getData(url)
		self.p2pSend()
		conn.send(response)
		conn.close()

	def handleNotExistindgUrl(self, url, host, data, recv_data, conn):
		logging.info("Cache MISS: "+ url)
	
		response = getHttp(host, data, self.buffer_size)
		self.cache.cachePush(url, response)
		self.p2pSend()
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
		logging.info("Requisicao de %s para %s" % (addr, url))

		# Caso o campo 'no-cache' do cabecalho esteja evidente em 'pragma' ou 'cache-control', nao armazenar em cache
		if self.cache.existingUrl(url):
			self.handleExistingUrl(url, host, data, recv_data, conn)
		else:
			self.handleNotExistindgUrl(url, host, data, recv_data, conn)


