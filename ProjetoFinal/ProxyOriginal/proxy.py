import socket, logging 
from thread import start_new_thread
from cache import Cache
from util import *

# Configurar o logging

logging.basicConfig(filename = 'proxy.log', filemode='a',format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

log = logging.getLogger('proxy')

class ServidorProxy():
	"""docstring for ServidorProxy"""
	def __init__(self):
		self.port = 54321
		self.buffer_size = 8192
		self.conexoes = 10
		self.cacheSize = 999999999
		self.cache = Cache(self.cacheSize)
		self.host = "localhost"
	def start(self):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind((self.host, self.port))
			sock.listen(self.conexoes)
		except Exception, e:
			print "Erro ao iniciar o servidor Proxy"
			print e
			return
		print "|****************************************|"
		print"|\tHTTP Proxy Server\t\t |\n|\tPort: %d\t\t\t |\n|\tCache Size: %ld\t\t |\n|\tHost: %s\t\t\t |" % (self.port, self.cacheSize, self.host)  
		print "|****************************************|"

		while True:
			conn, addr = sock.accept()
			data = conn.recv(self.buffer_size)
			start_new_thread(self.requestHandler, (data, conn, addr))

	def requestHandler(self, data, conn, addr):

		#Fazer o parsing da requisicao do cliente, que retorna um dicionario de dados chave-valor
		recv_data = parseHeader(data)
		response = ""
		# Nao continuar com o metodo nao implementado GET.
		if recv_data['method'] != 'GET':
			notImplementedMethod(conn)
			return

		# Recuperar url e hpst do servidor requisitado pelo cliente
		url = recv_data['url']
		host = recv_data['Host']
		log.info("Requisicao de %s para %s" % (addr, url))

		# Caso o campo 'no-cache' do cabecalho esteja evidente em 'pragma' ou 'cache-control', nao armazenar em cache
		
		if self.cache.existingUrl(url):
				
			# Caso nao tenha o campo If-Modified-Since, apenas puxa o elemento do cache
			log.info("Cache HIT: " + url)
			response = self.cache.getData(url)
		else:
			log.info("Cache MISS: "+ url)
			
			if 'Cache-Control' in recv_data.keys() and recv_data['Cache-Control'] == 'no-cache':
				log.info("Cache-Control - 'no-cache'")
				response = getHttp(host, data, self.buffer_size)
			else:
				response = getHttp(host, data, self.buffer_size)
				self.cache.cachePush(url, response)

		conn.send(response)
		conn.close()
