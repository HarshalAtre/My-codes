from operator import truediv
from tkinter.messagebox import QUESTION


# QUESTION 3
text=input("enter your text : ", )
span=False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
    spam=True
else:
    spam=False
 
if(spam):
    print("this is spam")
else: 
    print( "this is not a spam")





















