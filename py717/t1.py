'''
定义以下函数：
	1.求得一个整型数的平方
	2.获取字符串的最大字符
	3.求得两个整型的最大公约数
'''

def pingfang(n):
	return n**2
def MaxString(s):
	#sjdkjkskl
	l = len(s)
	ma = s[0]
	for i in range(1,l):
		if ma < s[i]:
			ma = s[i]
	return ma
print(MaxString("hgahjkkkk"))
def gongyeushu(a,b):
	while True:
	# 8 9
		c = a % b
		if c== 0:
			break
		else:
			a =b
			b = c
		return c

print(gongyeushu(24,16))
	
