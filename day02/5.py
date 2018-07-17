#遍历100~1000之间的每一个数
cnt = 0

for i in range(100,1001):
	flag = True
	for j in range(2,i):
		if i%j==0:
			flag = False
			break
	if flag:
		cnt +=1
print(cnt)
