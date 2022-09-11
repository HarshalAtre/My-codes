class emp:
    company="google"

    def __init__(self, name , salary , subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit

        print('employee is registered')  #just run without any command to print it still prints for self

    #but for printing others than self we need to give commands
    
    def details(self):
        print(f'the name is {self.name}')
        print(f'the salary is {self.salary}')
        print(f'the subunit is {self.subunit}')



    def getsalary(self):#if self not added throws error

        print(f'the guy in {self.company} makes {self.salary}')
    @staticmethod

    def greet():#-->no need to put self in static ,
        print ('hello sir')


harshal=emp("harshal",100,'yt')
#  we have to command for others than self

harshal.details()



