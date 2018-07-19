import random
t = random.randint(0,10)
i =0
while i<3:
	guess = int(input("请输入你一个10以内的数字："))
	if t==guess:
		print("厉害了！500万属于你")
		break
	elif guess > t:
		print("大了，再给你一次机会")
	else:
		print("大胆一点")
	i+=1
