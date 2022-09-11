class person:
    country='india'
    def breath():
        print('I m breating...')

class employee(person):
    company='youtube'
    
    def breath(self):
        print('I m a programmer and luckily im breathing...')

class programmer(employee):
    company='google'

    def breath(self):
        print('I am a programmer and i am breating++')

p=person

e=employee()
pr=programmer()

p.breath()
e.breath()
pr.breath()

print(pr.country)#takes from directly person as its connected to prson through employee

# basicaliy its just like grandfather-->father-->son.

