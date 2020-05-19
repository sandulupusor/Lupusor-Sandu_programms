import random

print("Lets play rock paper scissors")

seq=['rock','paper','scissors']
a=0
b=0

while a<3 and b<3:
    PC=random.choice(seq)
    player=input()
    if player not in seq:
        print("Invalid input")
    if player==PC:
        print("Draw")
    elif player=='rock' and PC=='paper':
        print("PC wins")
        b+=1
    elif player=='rock' and PC=='scissors':
        print('Player wins')
        a+=1
    elif player=='paper' and PC=='scisssors':
        print("PC wins")
        b+=1
    elif player=='paper' and PC=='rock':
        print('Player wins')
        a+=1
    elif player=='scissors' and PC=='rock':
        print("PC wins")
        b+=1
    elif player=='scissors' and PC=='paper':
        print('Player wins')
        a+=1
if a==3:
    print("Player won")
else:
    print("PC won")
   