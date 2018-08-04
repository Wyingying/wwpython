'''
生成器函数实现可迭代对象
实现一个可迭代对象的类，它能迭代出给定范围内的所有元素数
'''
class PrimeNumbers:
	def __init__(self,start,end):
		self.start = start
		self.end = end
	def	isPrimeNum(self,k):
		if k < 2:
			return False
		for i in range(2,k):
			if k % i ==0:
				return True
		return False
	def __iter__(self):
		for k in range(self.start,self.end + 1):
			if not self.isPrimeNum(k):
				yield k

for x in PrimeNumbers(8,20):
	print(x)
		

