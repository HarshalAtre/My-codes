import random

randNumber=random.randint(1,100)
userguess=int(input('Enter your Guess in Between 1 To 100 : '))

Guess=1

while userguess<randNumber or userguess>randNumber:


 if userguess<randNumber:
    print('You Guessed it Wrong!!! Try higher number')

 else:
    print('You Guessed it Wrong!!! Its a lower number ')  
    
 Guess=Guess+1

 userguess=int(input('Enter your Guess : '))
  
 
 
print('You Guessed It Right')

print(f'It Took You {Guess} Guesses To Guess The Number')

with open('C:\python\project 2\hiscore.txt') as f:
    hiscore=int(f.read())

if Guess<hiscore:
    print('You have just broke the high score')
    with open('C:\python\project 2\hiscore.txt','w') as f:
        f.write(str(Guess))
