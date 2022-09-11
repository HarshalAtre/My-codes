try:
    a=int(input('Enter a Number : " '))
    c=1/a
    print(c)

except ValueError as e:# diffrent handling for different type of errors.
    print('Please enter a valid value')

except ZeroDivisionError as e:
    print('You cannot divide any number with 0')

except Exception as e :
    print ('An error occured , Please try again')


print('Thanks for using my program')



