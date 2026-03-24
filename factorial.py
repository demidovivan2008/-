a=int(input())
n=0
for i in range(5,a+1,5):
	while i!=0:
		if i%5==0:
			n=n+1
		i=i/5
print(n)