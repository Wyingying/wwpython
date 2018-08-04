'''
装饰器对有参数的函数进行装饰
'''
def func(functionName):
	print("---func--1---")
	def func_in():
		print("---func_in--1")
		ret=functionName()
		print("---func_in--2")
		return ret
	print("---func--2---")
	return func_in

def test():
	print("---test---")
	return "hello world"

ret = test()
print("test return value is ",ret)


