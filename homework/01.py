'''
读入10个学生的成绩，要求在0~100之间，定义一个函数,
统计10个学生成绩的平均分，最高分，和最低分

'''
def average():
	i = 0
	nun=[]
	while i< 10:
		try:
			n = int(input("请输入第{}个学生的成绩(0~100)：".format(i+1)))
		except Exception:
			continue
		if  not(0<= n <=100):
			continue
		
		nun.append(n)
		i=i+1
	number = len(nun)
	Manum=nun[0]
	Minun=nun[0]
	Alnun=nun[0]
	j=1
	for j in range(number):
		Alnun+=nun[j]
		if nun[j]> Manum:
			Manum=nun[j]
		if nun[j]< Minun:
			Minun=nun[j]
	aver = Alnun/number
	return aver,Manum,Minun

aver,Manum,Minun=average()
print("这10个人平均分为：{}最高分：{}最低分:{}".format(aver,Manum,Minun))
