'''
装饰器对有参数的函数进行装饰
'''
def func_arg(arg):
	def func(functionName):
		def func_in():
			print("--记录日志--arg=%s"%arg)
			functionName()
		return func_in
	return func
#1.先执行func_arg("heihei")函数，这个函数return的结果是func这个函数的引用
#2.@func
#3.使用@func对test进行装饰
@func_arg("heihei")
def test():
	print("---test---")

test()

