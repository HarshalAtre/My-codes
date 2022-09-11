o=int(input('enter your no. 1 '))
p=int(input('enter your no. 2 '))
i=int(input('enter your no. 3 '))



def f(a,b,c):
    if(a>b):
        y=a
    else:
        y=b
    if(y>c):
        return (f'{y} is greater')
    else:
        return(f'{c} is greater')
y=f(p,o,i)
print(y)




