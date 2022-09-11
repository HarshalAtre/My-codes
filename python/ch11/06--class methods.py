class employee:
    company='kissan'
    salary='100'
    location='mumbai'

    # def changesalary(self,sal):-----> doesn't change class attribute but adds intance attribute.
    #     self.salary=sal

    # def changesalary(self,sal):#------> changes class attribute.
    #     self.__class__.salary=sal

    @classmethod #----->this is an alternate and easy method

    def changesalary(cls,sal):#------> changes class attribute.
        cls.salary=sal

e=employee()
print(e.salary)
e.changesalary(455)
print(e.salary)
print(employee.salary)