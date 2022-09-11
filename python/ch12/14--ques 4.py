a=(input('Enter a number to divide: '))
b=(input('Enter a number to whom you have to divide with: '))



try:
    a=int(a)
    b=int(b)
    print(a/b)

except ZeroDivisionError:
 if a==0 and b==0:
    print('Not Defined')
 else:
    print('Infinite')

except ValueError:
    print('Please enter a valid value')







