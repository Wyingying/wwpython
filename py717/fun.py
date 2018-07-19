
def mysqure(n,m=2):
	return n ** m

print(mysqure(5,4))
print(mysqure(9))


def cale(n,*arg):
	s = 0
	s= s+n
	for i in arg:
		s+=i
	return s
print(cale(4,8,33,54,12))

def test(arg1,*arg3,arg2=8):
	print(arg1,arg2)
	for i in arg3:
		print(i)
test(3,7,6,5,3,4,arg2=7)	
