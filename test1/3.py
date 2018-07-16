#-*-coding:UTF-8-*-
s = input("请输入一个字符串:")
i=0
U=0
L=0
N=0
while i < len(s):
	if s[i].isupper():
		U+=1
		
	elif s[i].islower():
		L+=1
		
	elif s[i].isdigit():
		N+=1
	
	
	i+=1
print("这个字符串中大写字母的个数为%d,小写字母的个数为%d,数字的个数为%d"%(U,L,N))
