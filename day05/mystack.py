'''
实现栈
'''
class Stack(object):
	def __init__(self):
		self.__list = []
	'''添加一个新的元素item到栈顶'''
	def push(self,item):
		self.__list.append(item)
	'''弹出栈顶元素'''
	def pop(self):
		return self.__list.pop()
	'''返回栈顶元素'''
	def peek(self):
		if self.__list:
			return self.__list[-1]
		else:
			return None
	'''判断栈是否为空'''
	def is_empty(self):
		return self.__list == []
	'''返回栈的元素个数'''
	def size(self):
		return len(self.__list)

if __name__ == "__main__":
	s = Stack()
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	s.push(5)
	print(s.size())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.is_empty())
	print(s.pop())
	print(s.pop())
