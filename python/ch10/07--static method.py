class emp:
    company="google"

    def getsalary(self):#if self not added throws error
        print(f'the guy in {self.company} makes {self.salary}')
    @staticmethod
    def greet():#-->no need to put self in static ,
        print ('hello sir')
#we can make static methods as many as we want

nitin=emp()
nitin.salary= "110 k "

nitin.getsalary() #--> Emp.getsalary(nitin)

nitin.greet()






