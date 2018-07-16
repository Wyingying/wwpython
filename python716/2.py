#python判断语句在一句中执行，只能执行一条if判断
num = eval(input("请输入一个数字："))
print("{0}{1}一个偶数".format(num,"不是" if num %2 else "是"))
