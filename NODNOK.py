print("Программа для нахождения НОД и НОК")
a = int(input("Напишите первое число"))
b = int(input("Напишите второе число"))
def NOD(a,b):
	if a==b:
		return a
	if a>b:
		for i in range(a,0,-1):
			if a%i==0 and b%i==0:
				return i
	if a<b:
		for i in range(b,0,-1):
			if a%i==0 and b%i==0:
				return i
print("НОД = ", NOD(a,b))
def NOK(a,b):
	return (a*b)//NOD(a,b)
print("НОК = ", NOK(a,b))