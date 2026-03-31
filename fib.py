a=int(input())
n=[0,1]
if a<=0:
	print("None")
elif a==1:
	print(0)
elif a>0:
	for i in range(a-2):
		n.append(n[i]+n[i+1])
	print(n)