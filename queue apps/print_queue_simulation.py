import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from queue import Queue
import random

class Printer:
	def __init__(self, pages_per_minute):
		self.page_rate = pages_per_minute
		self.current_task = None
		self.time_remaining = 0

	def tick(self):
		if self.current_task != None:
			self.time_remaining -= 1
			if self.time_remaining <= 0:
				self.current_task = None

	def busy(self):
		if self.current_task != None:
			return True
		else:
			return False

	def start_next(self, new_task):
		self.current_task = new_task
		self.time_remaining = new_task.get_pages() * (60/self.page_rate)

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1,21)

	def get_stamp(self):
		return self.timestamp

	def get_pages(self):
		return self.pages

	def wait_time(self, current_time):
		return current_time - self.timestamp

#The main simulation

def simulation(seconds, ppm):
	lab_printer = Printer(ppm)
	print_queue = Queue()
	waiting_times = []

	for current_sec in range(seconds):
		
		if new_print_task():
			task = Task(current_sec)
			print_queue.enqueue(task)
		
		if (not lab_printer.busy()) and (not print_queue.isEmpty()):
			next_task = print_queue.dequeue()
			waiting_times.append(next_task.wait_time(current_sec))
			lab_printer.start_next(next_task)
		lab_printer.tick()

	avg_wait_time = sum(waiting_times)/len(waiting_times)
	print("Average waiting time %.2f secs with %d tasks remaining."%(avg_wait_time,print_queue.size()))

def new_print_task():
	if random.randrange(1,181) == 180:
		return True
	else:
		return False

for i in range(10):
	simulation(3600, 10)
