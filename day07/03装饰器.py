'''
两个装饰器的装饰先后顺序，和执行的先后顺序
'''

def w1(func):
	print("---正在装饰1----")
	def inner():
		print("----正在验证权限1-----")
		func()
	return inner

def w2(func):
	print("---正在装饰2----")
	def inner():
		print("----正在验证权限2-----")
		func()
	return inner
#只要python解释器执行到了这个代码，那么就会自动的进行装饰，而不是等到调用的时候才装饰的
@w1
@w2
def f1():
	print("----f1---")
#在调f1之前，已经开始进行装饰了
f1()
