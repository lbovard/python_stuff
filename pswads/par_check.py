from Stack import *

def parChecker(symbolString):
	s=Stack()
	balanced = True # default
	index =0 
	while index < len(symbolString) and balanced:
		symbol=symbolString[index]
		# if (,{,[ push onto stack
		if symbol in "({[":
			s.push(symbol)
		else:
			# if stack is empty, imbalance 
			if s.isEmpty():
				balanced = False
			else:
				top=s.pop()
				if not matches(top,symbol):
					balanced = False

		index = index+1

	# balanced and no ( present 
	if balanced and s.isEmpty():
		return True
	# otherwise unbalanced ( present
	else:
		return False

def matches(a,b):
	"""	checks whether symbol a corresponds to 
			opposite symbol b. e.g. a=) b=( returns true
			a={ b = ] returns false"""
	opens="({["
	closes=")}]"
	return opens.index(a) == closes.index(b)
print parChecker('()()()()()')
print parChecker('()')
print parChecker('()))))((()()()()()()(')
print parChecker('{{{[[[()}}]]]}')
print parChecker('{{[][]({[]})}}')
