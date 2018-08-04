#
import random
cn =[0]*11
sumn=[]
for i in range(0,20):
	sumn.append(random.randint(0,100))
	print(sumn[i],end=' ')
	cn[sumn[i]//10]+=1

print()
print("100:",end=' ')
print(cn[10]*'*')
for i in range(9,-1,-1):
	print("{}~{}".format(i*10,i*10+9),end=' ')
	print(cn[i]*'*')
