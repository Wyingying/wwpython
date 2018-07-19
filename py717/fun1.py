'''
汉诺塔问题
'''
cnt = 0
def move(m,n):
	global cnt
	cnt += 1
	print(m,"--->",n)
def hano(n,a,b,c):
	if n == 1:
		move(a,b)
		return None
	hano(n-1,a,c,b)
	hano(1,a,b,c)
	hano(n-1,c,b,a)
hano(3,'a','b','c')
print("共{}次".format(cnt))
