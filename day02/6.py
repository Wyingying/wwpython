
name = input("请输入一个名字：")

for s in name:
	if not(s.isalpha() or s.isdigit() or s=='_'): 
		print("你的名字不符合规格")
else:
	print("你的名字录入成功")
	
