class person:
    country='india'
    
   
    def breath():
        
        print(f'I m breating... ')

class employee(person):
    company='youtube'
    
    def __init__(self):
        print('intializing employee...')
        super().__init__()
    
    def breath(self):
       
        print('I m a programmer and luckily im breathing...')

class programmer(employee):
    company='google'

    def __init__(self):
        print('intializing programmer...')
        super().__init__()

    def breath(self):

        super().breath()#first prints its parent class attribute

        print('I am a programmer and i am breating++')

# p=person

# e=employee()
pr=programmer()

# p.breath()
# e.breath()
# pr.breath()


