'''
循环链表的实现
'''
class Node(object):
	'''节点'''
	def __init__(self,item):
		self.elem = item
		self.next = None

class SingleCycleLinkList(object):
	'''单项循环链表'''
	def __init__(self,node=None):
		self.__head = node
		if node:
			node.next = node
	'''链表是否为空'''
	def is_empty(self):
		return self.__head==None
	'''链表的长度'''
	def length(self):
		if self.is_empty():
			return 0
		#cur游标用来移动遍历节点
		cur = self.__head
		#count记录数量
		count = 1
		while cur.next != self.__head:
			count+=1
			cur = cur.next
		return count
	'''遍历整个链表'''
	def travel(self):
		cur = self.__head
		if self.is_empty():
			return 
		while cur.next != self.__head:
			print(cur.elem,end=" ")
			cur = cur.next
		#退出循环，cur指向尾节点，但是尾节点的元素未打印
		print(cur.elem)
	'''链表头部添加元素'''
	def add(self,item):

		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			#退出循环后，cur指向尾节点
			node.next = self.__head
			self.__head = node
			cur.next = node
	'''链表尾部添加元素'''
	def append(self,item):
		node = Node(item)
		cur = self.__head
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			while cur.next!= self.__head:
				cur = cur.next
			cur.next=node
			node.next=self.__head 
	'''指定位置添加元素'''
	def insert(self,pos,item):
		if pos < 0:
			self.add(item)
		elif pos > self.length() -1:
			self.append(item)
		else:
			pre = self.__head
			count = 0
			while count < (pos-1):
				count += 1
				pre = pre.next
			#当循环退出后，pre指向pos-1位置
			node = Node(item)
			node.next = pre.next
			pre.next = node		
	'''删除节点'''
	def remove(self,item):
		if self.is_empty():
			return 
		cur = self.__head
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				if cur == self.__head:
					# 头节点的情况
					#找尾节点
					rear = self.__head
					while rear.next !=self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
					
				else:
					pre.next = cur.next
				return 
			else:
				pre = cur
				cur = cur.next
		 #退出循环，cur指向尾节点
		if cur.elem == item:
			if cur == self.__head:
				self.__head = None
			else:
				pre.next = cur.next
	'''查找节点是否存在'''
	def search(self,item):
		if self.is_empty():
			return False
		cur = self.__head
		while cur != self.__head:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		#退出循环，cur指向尾节点
		if cur.elem == item:
			return True	
		return False

if __name__ == "__main__":
	ll = SingleCycleLinkList()
	print(ll.is_empty())
	print(ll.length())
	ll.append(2)
	ll.append(3)
	ll.add(8)
	ll.append(4)
	ll.append(5)
	ll.insert(-1,9)
	ll.travel()
	print()
	ll.insert(2,100)
	ll.travel()
	print()
	ll.insert(10,300)
	ll.travel()
	print()
	ll.remove(9)
	ll.travel()
	print()
	ll.remove(300)
	ll.travel()
	print()
