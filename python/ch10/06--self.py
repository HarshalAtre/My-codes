class emp:
    company="google"
    
    def getsalary(self):#if self not added throws error
        print(f'the guy in {self.company} makes {self.salary}')

nitin=emp()
nitin.salary= "110 k "

nitin.getsalary()#--> Emp.getsalary(nitin)








