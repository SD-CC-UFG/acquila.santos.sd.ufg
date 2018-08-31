import threading
from Queue import Queue, Empty


class Worker(threading.Thread):

	def __init__(self, pool):
		super(Worker, self).__init__()
		self.pool = pool
		self.executing = 0

	def start(self):
		self.executing = 1
		super(Worker, self).start()

	def run(self):
		while self.executing == 1:
			try:
				func, args, kwargs = self.pool.jobs.get(block=False)
			except Empty:
				continue
			else:
				try:
					result = func(*args, **kwargs)
					self.pool.results.put(result)  
				except Exception, e:
					self.executing = 0
					raise e

class ThreadPool(object):

	def __init__(self, nThread = 5):
		self.thread_list = []
		self.nThread = nThread
		self.jobs = Queue()
		self.results = Queue()
		self.start()

	def start(self):
		for _ in range(self.nThread):
			self.thread_list.append(Worker(self))
		for j in self.thread_list:
			j.start()	

	def insert_job(self, func, *args, **kwargs):
		self.jobs.put((func, args, kwargs))
			