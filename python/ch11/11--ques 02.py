class animals:
    print('I am may be domestic or wild')

class pets(animals):
    print("But don't worry i am a pet")

class dog(pets):

    def __init__(self):
        print('My breed is german shepard')

    @staticmethod
    def bark():    
        print('Bow Bow!!!')

tommy=dog()
tommy.bark()





