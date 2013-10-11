class stack(object):
	"""A simple queue class"""

	def __init__(self):
		self.stack = []
    
	def add(self, newItem):
		self.stack.append(newItem)

	def get(self):
		lastIndex = len(self.stack) - 1
		elem = self.stack[lastIndex]
		self.stack.pop(lastIndex)
		return elem

	def length(self):
		return len(self.stack)

	def min(self):
		return "NOT YET IMPLEMENTED"


# # a 
# print "========================="
# a = stack()
# [a.add(x) for x in range(10)]

# print "a 10 element sequential stack: "
# print a.stack

# print
# print "added a 5:"
# a.add(5)
# print a.stack

# print 
# print "got from stack:"
# print a.get()
# print a.stack

class queue(object):
	"""A simple queue class"""

	def __init__(self):
		self.q = []
    
	def add(self, newItem):
		self.q.append(newItem)

	def get(self):
		elem = self.q[0]
		self.q.pop(0)
		return elem

# a 

# a = queue()
# [a.add(x) for x in range(10)]

# print a.q
# print "a 10 element sequential queue: "

# print
# print "added a 5:"
# a.add(5)
# print a.q

# print 
# print "got from queue:"
# print a.get()
# print a.q


class queueS(object):
	def __init__(self):
		self.incomingStack = stack()
		self.outgoingReversedStack = stack()

	def add(self, newItem):
		self.incomingStack.add(newItem)

	def get(self):
		length = self.outgoingReversedStack.length()
		if length == 0:
			for i in range(length)
			 	self.outgoingReversedStack.add(self.incomingStack.get())

		return self.outgoingReversedStack.get()


		










