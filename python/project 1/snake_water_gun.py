from gzip import compress
import random

# Snake,Water and Gun/ Rock,Paper and Scissors

def game(comp,you):
    if you==comp:
        return None
    elif comp=="s":
        if you=="w":
           return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="s":
           return True
        elif you=="g":
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":    
            return True

     
 
print('comp chose its choice')

ra=random.randint(1,3)
if ra==1:
    comp="s"
elif ra==2:
    comp="w"
elif ra==3:
    comp="g"

you=input('your turn: Snake(s) , Water(w) or Gun(g)?')
a=game(comp,you)
print(f'computer chose {comp}')
print(f'you chose {you}')
if a==None:
    print("The game is a tie!")
elif a:
    print('You won the game! ')
else:
    print('You lost the game!')














