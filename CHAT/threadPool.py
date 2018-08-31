import threading
from Queue import Queue, Empty


class Worker(threading.Thread):

	def __init__(self, pool):
		super(Worker, self).__init__()
		self.pool = pool
		self.executing = 0

	''' Override do metodo start da biblioteca threading '''
	def start(self):
		self.executing = 1
		super(Worker, self).start()
	''' Override do metodo run da biblioteca threading '''
	def run(self):

		''' Executar o laco enquanto a thread esta em execucao '''
		while self.executing == 1:
			try:
				''' Retorna um item da fila quando ele estiver imediatamente disponivel '''
				func, args, kwargs = self.pool.jobs.get(block=False)
			except Empty:
				continue
			else:
				try:
					''' Executa o processo '''
					result = func(*args, **kwargs)
					''' Coloca o resultado da execucao na fila results '''
					self.pool.results.put(result)  
				except Exception, e:
					self.executing = 0
					raise e

class ThreadPool(object):

	def __init__(self, nThread = 5):
		
		self.thread_list = [] # Lista de threads pre alocadas
		self.nThread = nThread # Numero de threads
		self.jobs = Queue() # Fila de processos a serem executados pelas threads
		self.results = Queue() # Fila de resultados dos processos
		self.start() # Executa a thread assim que o objeto de ThreadPool eh criado

	def start(self):
		''' Adicionar as threads na lista de threads e inicia-las de forma apropriada em Worker '''
		for _ in range(self.nThread):
			self.thread_list.append(Worker(self))
		''' Iniciar os processos '''
		for j in self.thread_list:
			j.start()	

	def insert_job(self, func, *args, **kwargs):
		self.jobs.put((func, args, kwargs))
			
