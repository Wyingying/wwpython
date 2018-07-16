#-*-coding:UTF-8-*-
str1=input("请出入第一个字符串:")
str2=input("请出入第二个字符串:")
l1=0
l2=0
if len(str1) - len(str2) >=0:
	while l2 < len(str2):
		if ord(str1[l2])>ord(str2[l2]):
			print("第一个字符串大于第二个字符串")
			break
		elif ord(str1[l2])<ord(str2[l2]):
			print("第二个字符串大于第一个字符串")
			break
		
		print("第一个字符串大于第二个字符串")
		l2+=1
		
elif len(str2) - len(str1):
	while l1 < len(str2):
		if ord(str1[l1])>ord(str2[l1]):
			print("第一个字符串大于第二个字符串")
			break
		elif ord(str1[l1])<ord(str2[l1]):
			print("第二个字符串大于第一个字符串")
			break
		
		print("第二个字符串大于第一个字符串")
		l1+=1
				
else:
	print("两个字符串相等")
