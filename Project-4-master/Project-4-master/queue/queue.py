try:	
	class Queue:
		#define __init__ function
		def __init__(self):
			self.queue = list()
			self.head = 0
			self.tail = 0
		
		#add data
		def addtoqueue(self, data):
			self.queue.insert(0, data)
			self.tail += 1
			return True

		#size of queue
		def size(self):
			return len((list(self.queue)))

		#remove last item from tail
		def popfromqueue(self):
			if len(self.queue)>0:
				return self.queue.pop()
			return("Queue is empty!")


	newitem = Queue()
	newitem.addtoqueue("Audi R8")
	newitem.addtoqueue("Subaru WRX STI")
	newitem.addtoqueue("Hyundai Genesis")
	newitem.addtoqueue("Old 2002 Camry")
	print(list(newitem.queue))
	print("Manager: 'Let's start emptying this Drive Thru!'")


	newitem.popfromqueue()
	print(list(newitem.queue))
	print("Employee: 'Woah! Did you see that Audi before it drove away???'")
	newitem.popfromqueue()
	print(list(newitem.queue))
	newitem.popfromqueue()
	print(list(newitem.queue))
	print("Manager: 'Now we're getting somewhere'")

	print("Manager: 'How many cars in the line now?'")
	print("Employee: '" + str(newitem.size()) + "'") 
except:
	print("You have caused an error. Please check your syntax and try again")

