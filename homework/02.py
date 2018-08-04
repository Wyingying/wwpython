'''
2.随机产生10个10以内的整型数，存放到列表中，将列表中的最大值放在列表的最后。
'''
import random 
l = []
for i in range(0,10):
	l.append(random.randint(0,9))
print(l)
m = max(l)
l.remove(m)
l.append(m)
print(l)
