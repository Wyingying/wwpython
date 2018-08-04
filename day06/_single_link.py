'''
单链表的实现
'''
class Node(object):
	'''节点'''
	def __init__(self,item):
		self.elem = item
		self.next = None

class SingleLinkList(object):
	'''单链表'''
	def __init__(self,node=None):
		self.__head = node
	'''链表是否为空'''
	def is_empty(self):
		return self.__head==None
	'''链表的长度'''
	def length(self):
		#cur游标用来移动遍历节点
		cur = self.__head
		#count记录数量
		count = 0
		while cur!=None:
			count+=1
			cur = cur.next
		return count
	'''遍历整个链表'''
	def travel(self):
		cur = self.__head
		while cur !=None:
			print(cur.elem,end=" ")
			cur = cur.next
	'''链表头部添加元素'''
	def add(self,item):
		node = Node(item)
		node.next = self.__head
		self.__head = node
	'''链表尾部添加元素'''
	def append(self,item):
		node = Node(item)
		cur = self.__head
		if self.is_empty():
			self.__head = node
		else:
			while cur.next!=None:
				cur = cur.next
			cur.next=node 
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
		cur = self.__head
		pre = None
		while cur != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
				else:
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next
		 
	'''查找节点是否存在'''
	def search(self,item):
		cur = self.__head
		while cur !=None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next	
		return False

if __name__ == "__main__":
	ll = SingleLinkList()
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
