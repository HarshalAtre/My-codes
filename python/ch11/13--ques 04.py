# (a+bi)(c+di)=(ac-bd) + (ad+bc)

class complex:
    def __init__(self,r,i):
        self.real=r
        self.img=i

    def __add__(self,c):
        return complex(self.real + c.real,self.img+c.img)
    
    def __mul__(self,c):
        mulreal=self.real*c.real - self.img*c.img
        mulimg=self.real*c.img + self.img*c.real
        return complex(mulreal,mulimg)

    def __str__(self):
        if(self.img<0):
            return f'{self.real} - {-self.img} i'
        else:
            return f'{self.real} + {self.img} i'

c1=complex(1,-4)
c2=complex(331,-37)
print(c1+c2)
print(c1*c2)