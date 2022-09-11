from calendar import c


class employee:
    company='google'
    def detail(self):
        print(f'this is an employee')

class programmer(employee):
    lang ='python'
    def lang(self):
        print(f'the language used is {self.lang}')

    def detail(self):
        print('this is a programmer')
e=employee()
p=programmer()

e.detail()
p.detail()# prints the thign in employee class cause programmer can use all attributes of employee.
print(p.company) #prints the thign in employee class cause programmer can use all attributes of employee
p.detail() # now here it print the attribute in programmer class it first checks in programmer then goes to parent class
