a=input('Enter your 1st file name : ')


with open(f'C:\python\ch9\{a}') as f:
    r=f.read().lower()
    with open(f'C:\python\ch9\copy.txt') as d:
     t=d.read().lower()
    if r in t:
        print('yes, files are identical')
    else:
        print('No,files are not identical')







