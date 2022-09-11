class employee:
    company='hp gas'
    salary=6000
    bonus=500
    total=6500

    @property
    def total(self):
        return self.salary + self.bonus

    @total.setter
    def total(self,val):    
        self.bonus= val-self.salary

e=employee()
print(e.total)
e.total=6100
print(e.bonus)




