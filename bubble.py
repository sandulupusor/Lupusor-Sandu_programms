import random

n=int(input("Number of numbers="))
a=[]
for i in range(n):
    a.append(random.randint(0,n))
print(a)

q=1

while q:
    k=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            b=a[i+1]
            a[i+1]=a[i]
            a[i]=b
            k+=1
    if k==0:
        q=0

print(a)