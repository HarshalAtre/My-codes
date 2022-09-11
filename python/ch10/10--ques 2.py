


class calculator:
    def __init__(self , num):
        self.num=num
    
    def sq(self):
        print(self.num*self.num)
    def cube(self):
        print(self.num*self.num*self.num)
    def sqrt(self):
        print(self.num**0.5)
a=calculator(9)         

a.sq()
a.cube()
a.sqrt()





