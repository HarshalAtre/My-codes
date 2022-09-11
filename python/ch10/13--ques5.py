

class train:
    def __init__(self,name,fare,seats):

        self.name=name
        self.fare=fare
        self.seats=seats
        
        # print(f'the name is {self.name}\n the fare is {self.fare}\n,the no. of seat
    def status(self):
        
        print(f'''*********
        the name of the train is {self.name}
        the seats available are {self.seats}
        the fare is {50}
        **********''')
    def book(self):
        if self.seats>0:
            print(f'booked \n your ticket no. is {self.seats}')
            self.seats=self.seats-1
        else:
            print('Sorry train is full')
            
    def cancel(self):
        print('your ticket is cancelled')        
        self.seats=self.seats+1

    
            

stabdi=train('shatabdi',50,10)

stabdi.book()
stabdi.book()
# stabdi.status()

stabdi.cancel()
stabdi.status()






