while (True):
 a=(input('Enter Your No.: '))
 print('Press q to exit')
 if(a=='q'):
    break
 try:
    print('Trying...')
    a=int(a)
    if a>6:
        print('You enter a number greater than 6')
 except Exception as e:
    print(f'You Entered an invalid value : {e} ')

print('Thanks for playing!')