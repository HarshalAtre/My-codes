def re(n):
    if n==1 :
        return 1
    elif(n==0):
       return 0
    else:
        return n+re(n-1)

a=re(int(input('Enter your no. : ')))
print(a)














