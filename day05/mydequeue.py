'''
python 实现双端队列
'''

class Deque(object):
	def __init__(self):
		self.__list = []	
	'''从列表头部添加一个item元素'''
	def add_front(self,item):
		self.__list.insert(0,item)
	'''从列的队尾添加一个item元素'''
	def add_rear(self,item):
		self.__list.append(item)
	'''从队列头部删除一个元素'''
	def remove_front(self):
		return self.__list.pop(0)
	'''从队列尾部删除一个元素'''
	def remove_rear(self):
		return self.__list.pop(-1)
	'''判断一个队列是否为空'''
	def is_empty(self):
		return self.__list == []
	'''返回一个队列的长度'''
	def size(self):
		return len(self.__list)

if __name__ == "__main__":
	s = Deque()
	s.add_front(1)
	s.add_front(2)
	s.add_rear(3)
	s.add_rear(4)
	s.add_front(5)
	print(s.remove_front())
	print(s.remove_front())
	print(s.remove_rear())
	print(s.remove_rear())
	print(s.remove_front())
