from queue import Empty
from multiprocessing import Process,Queue
from threading import Thread

class eventEngine():

	def __init__(self):
		self.__eventQueue = Queue()
		self.__commander = Queue()
		self.__response ={'Stop':self.Stop}
		self.__active = False
		self.__threads = {}
		self.__procs = {}
		# self.__handlers = {}

	def __Run(self):
		while self.__active:
			print('ALive')
			try:
				command = self.__commander.get(block=True,timeout=1)
				self.__response[command]()
			except Empty:
				pass
			try:
				event = self.__eventQueue.get(block=True,timeout=1)
				self.__EventProcess(event)
			except Empty:
				pass

	def __EventProcess(self,event):
		if event.type_ == 'Proc':
			starter = Process(target = event.func,args=(self.Listen,))
			self.__procs[event.name]=starter
		elif event.type_ == "Thread":
			starter = Thread(target = event.func)
			self.__procs[event.name]=starter
		starter.start()
		# if event.type_ in self.handlers:
		# 	for handlers in self.__handlers[event.type_]:
		# 		handler(event)

	def Start(self):
		self.__active = True
		self.__Run()

	def Stop(self):
		self.__active = False
		for each in self.__threads.values()+self.__procs.values():
			try:
				each.terminate()
				each.join()
			except:
				print(each.pid,"Terminate error")
				each.join()
				pass

	def Listen(self,command=None,event=None):
		if command:
			self.__commander.put(command)
		if not event:
			self.__eventQueue.put(event)


class Event():

	def __init__(self,name,type_,func):
		self.name = name
		self.type_  = type_
		self.func = func
