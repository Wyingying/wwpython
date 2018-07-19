'''
3个红球 3个蓝球4个黄球
从中取出8个球 三种球的个数情况
'''
nun =0
#红球
for red in range(4):
	#蓝球
	for blue in range(4):
		#黄球
		for yello in range(5):
			if red + blue + yello ==8:
				print("红球:{}蓝球:{}黄球:{}".format(red,blue,yello))
				nun+=1
print("共有多少中情况{}".format(nun))
