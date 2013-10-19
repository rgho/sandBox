
# PROB 1
def recursiveAddList(plist):
	if plist == []: return 0
	return plist.pop(0) + recursiveAddList(plist)

#print recursiveAddList(range(100))



def lastIndexOf(pItem, pList):
	if pList == []: return -1

	if pList[len(pList)-1] == pItem: 
		return len(pList)-1
	else:
		pList.pop()
		return lastIndexOf(pItem, pList)

print lastIndexOf(5,[1,2,3,4,5,5,6,7]) 



def addBinTree(pTree):
	# CLOSE BUT DOES NOT WORK.
	#BASE CASE: if thisBranch is empty, return parent value
	if pTree[1] == ((),()): 
		return pTree[0]
	else:
		return addBinTree(pTree[1][0]) + addBinTree(pTree[1][1]) + pTree[0]
#addBinTree((1, (2, (), ()), (3, (4, (), ()), (5, (), ()))))


def fibunacci(n):
	if n == 0: return 0
	if n == 1: return 1
	return fibunacci(n-1) + fibunacci(n-2)

print fibunacci(5)



fib = dict()
fib[0] = 0
fib[1] = 1

def memFib(n):


	if n in fib:
		return fib[n]
	
	fib[n] = memFib(n-1) + memFib(n-2)
	return fib[n]

print memFib(10)









