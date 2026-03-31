a=int(input())
n=0
for i in range(5, a+1, 5):
    while i > 0 and i % 5 == 0:
        n += 1
        i //= 5
print(n)