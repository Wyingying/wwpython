'''
列表传参的应用
'''

def lstest(n,ls=[]):
	ls.append(n)
	return ls
#当列表作为参数传递时，传值不传递列表时，使用的默认列表是同一个，在函数循环
#过程中不消亡
l1= lstest(10)
l2 = lstest(123,['hello'])
l3=lstest('a')
print(l1)
print(l2)
print(l3)
'''
[10, 'a']
['hello', 123]
[10, 'a']

'''

'''
列表的生成式

'''

ls1= list(range(1,101))
print(ls1)
ls2 = []
for i in range(1,10):
	ls2.append(i*i)
print(ls2)
ls3 = [i*i for i in range(1,10)]

print(ls3)

ls4 = [i*i for i in range(1,10) if i % 2]

print(ls4)

#ABCD MNOP

l5 = [i+j for i in "ABCD" for j in "MNOP"]
print(l5)

