class library:
    
    #  def __init__(self,list):
    #     self.books=list
    
    def borrowbook(self,bookname): 
         self.book=bookname
         print('The Book is been issued to you , Please return it in 30 days')
         
        

class student:

    def returnbook(self,bookname):
        self.book=bookname
        print('Thanks for returning the book, Hope you enjoyed reading it')

central_library=library()
central_library.lib=['clrs','Algorithm','The Jungle Book','Avengers','Python Notes']

me=student()


while(True):
    print('=====Welcome to Central Library======')
    print('''
    1.look for the available books
    2.Borrow a book
    3.Return a book
    4.Donate a book
    5.Exit
    ''')
    
    choice=int(input('Please Enter your choice : '))

    if choice==1:
        print('Book present in library are :  ')
        for item,i in enumerate(central_library.lib):
            print('*'+i)
    
    elif choice==2:
     bookname=input('Enter the name of book to borrow : ')
     central_library.lib.remove(bookname)
     central_library.borrowbook(bookname)
    
    elif choice==3:
     bookname=input('Enter the name of book to return : ')
     central_library.lib.append(bookname)
     me.returnbook(bookname)

    elif choice==4: 
        bookname=input('Enter the name of book to donate : ')
        central_library.lib.append(bookname)
        print('Thanks For Donation!! , Have a great day ahead')

    elif choice==5:
        break

    else:
        print('Invalid Choice , Please follow the menu list!!!')