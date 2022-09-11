def greet(name):
    print(f'Good Morning, {name}')

# print(__name__)

if __name__=='__main__':# --> if we not do this,when we import the file for function (just like in M07--file2 ) the below part also gets printed 

    n=input('Enter Your name : ')
    greet(n)