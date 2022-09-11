class number:
   def __init__(self,num):
    self.num = num

   def __add__(self,num2):#-->defines how to add two number in our number class 
    print('lets add')
    return self.num +num2.num
    
   def __mul__(self,num2):#-->defines how to multiply two number in our number class 
    print('lets multiply')
    return self.num * num2.num
    
n1=number(4)
n2=number(6)
s=n1+n2#-->adds according to our methods not by regular integer method.
d=n1*n2
print(s)
print(d)
f=n1/n2
print(f)#-->throws error as till now no method is defined for division
