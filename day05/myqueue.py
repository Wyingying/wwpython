'''
python 实现队列
'''

class Queue(object):
	def __init__(self):
		self.__list = []	
	'''往队列中添加一个item元素'''
	def enqueue(self,item):
		self.__list.append(item)
	'''从队列头部删除一个元素'''
	def dequeue(self):
		return self.__list.pop(0)
	'''判断一个队列是否为空'''
	def is_empty(self):
		return self.__list == []
	'''返回一个队列的长度'''
	def size(self):
		return len(self.__list)

if __name__ == "__main__":
	s = Queue()
	s.enqueue(1)
	s.enqueue(2)
	s.enqueue(3)
	s.enqueue(4)
	s.enqueue(5)
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
