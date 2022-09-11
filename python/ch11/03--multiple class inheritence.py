class employee:
    company='visa'
    ecode=120

class freelancer:
    company='fiveer'
    level=2
    def upgradelevel(self):
        self.level=self.level +1
class programmer(freelancer,employee):
    name='vivek'

p=programmer()
print(p.ecode)#takes from employee class
print(p.level)#takes from freelancer class
p.upgradelevel()
print(p.level)
print(p.company)#prints 'fiveer' coz freelancer is written first in programmer so it gets the priority

