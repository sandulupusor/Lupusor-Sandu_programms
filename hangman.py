
word='anywordyouwant'
guess='_'*len(word)

k=6

while k>0:
    print(guess)
    a=input("letter only lower case ")
    for i in range (0,len(word)):
        if word[i]==a:
            guess=guess[:i]+a+guess[i+1:]
    if guess==word:
        print("You won")
        break
    if a not in word:
        k-=1   
    print("Lives ", k)     
if k==0:
    print("You lost")
