'''
3.随机产生密码：
	在26个大小写字母和10个数字组成的列表中，随机生成10个8位密码

'''

import random
ls=[]
for i in range(10):
	ls.append(str(i))
for i in range(26):
	ls.append(chr(ord('A')+i))
for i in range(26):
	ls.append(chr(ord('a')+i))
print(ls)

for i in range(10):
	pwd=''
	for j in range(8):
		pwd+=ls[random.randint(0,61)]
	print(pwd)	
