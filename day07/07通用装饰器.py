'''
通用装饰器
'''
def func(functionName):
	def func_in(*args,**kwargs):
		ret = functionName(*args,**kwargs)
		return ret
	return func_in
@func
def test():
	print("--tsst---")
	return "haha"
@func
def test2():
	print("--tsst---")

@func
def test3(a,b):
	print("--tsst---a=%d,b=%d"%(a,b))

ret = test()
print("test return value is ",ret)
ret2 = test2()
print("test return value is ",ret2)
ret3 = test3(11,22)

