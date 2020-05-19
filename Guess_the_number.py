import random

a=random.randint(0,20)

q=1
while q:
    b=int(input("Try "))
    if b<a:
        print("Higher")
    elif b>a:
        print("Lower")
    else:
        q=0
        print("Ai ghicit")    