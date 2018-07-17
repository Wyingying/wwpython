#商城打折

price = int(input("请输入购买的金额："))

if 50<=price<=100:
	t=price-price*0.1
	s=price*0.1
	print("{}打10%的折后的价格是{}优惠的价格是{}".format(price,t,s))
elif price > 100:
	t=price-price*0.2
	s=price*0.2
	print("{}打20%的折后的价格是{}优惠的价格是{}".format(price,t,s))
