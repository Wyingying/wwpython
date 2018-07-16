'''
模拟进度条
'''
import time

i = 0 
scale = 10

while i <= scale:
	js = i * '##'
	ws = (scale - i) * '--'
	print ("\r{:^3.0f} %[{}-->{}]".format(i/scale*100,js ,ws),end='')
	i +=1
	time.sleep(0.5)
