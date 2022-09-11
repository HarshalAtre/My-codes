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
p.detail()
print(p.company) 
p.detail() 
