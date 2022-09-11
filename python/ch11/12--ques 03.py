class employee:
    company='Google'
    salary=1000
    increment=1.5
    salaryafterincrement=1500

    @property
    def salaryafterincrement(self):
        return self.salary * self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self,val):
        self.increment= val/self.salary


e=employee()

e.salaryafterincrement=34500
print(e.increment)