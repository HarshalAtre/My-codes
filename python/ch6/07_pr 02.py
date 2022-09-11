from tkinter.messagebox import QUESTION


# QUESTION 2
a=int(input("Enter the marks for subject 1 :"))
b=int(input("Enter the marks for subject 2 :"))
c=int(input("Enter the marks for subject 3 :"))

t=(a+b+c)/300*100

if(t<40):
    print("Fail")

elif(a<33):
    print("Fail")
elif(b<33):
    print("Fail")
elif(c<33):
    print("Fail")
else:
    print("Pass")
    
