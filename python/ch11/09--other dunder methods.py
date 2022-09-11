class number:
   def __init__(self,num):
    self.num = num

   def __str__(self):
        return f'decimal number {self.num}'

   def __len__(self):
    return 1

n1=number(4)

print(n1)#-->prints 4 because it is defined
print(len(n1))#--> prints 1 coz its defined otherwise throws error







