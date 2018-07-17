#用户输入身高和体重，根据BMI（体重kg/身高m的平方）体质，体重过轻：低于18.5

m = int(input("请输入你的体重："))

h = int(input("请输入你的身高："))

B = h/m*m
if B<=18.5:
	print("体重过轻")
elif 18.5<B < 23.9:
	print("正常")
elif 24<B<27:
	print("过重")
elif 28<B<32:
	print("肥胖")
else:
	print("非常肥胖")
