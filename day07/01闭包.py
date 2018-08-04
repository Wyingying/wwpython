'''
闭包的认识
'''
def test(number):
	print("---1--")
	def test_in(number2):
		print("---2--")
		print(number+number2)
	print("---3--")
	return test_in

ret=test(100)
print("*"*20)
ret(9)
ret(2)
ret(90)
