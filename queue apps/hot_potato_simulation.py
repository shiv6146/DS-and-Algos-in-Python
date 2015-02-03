import sys
sys.path.append('/home/shiva/Documents/shiv/pythonds/')
from queue import Queue

def hot_potato(name_list, num):
	q = Queue()
	
	for name in name_list:
		q.enqueue(name)

	while q.size() > 1:
		for i in range(num):
			q.enqueue(q.dequeue())
		q.dequeue()
	
	return q.dequeue()

print hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)
print hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],3)