N=int(input('Enter your no. : '))

table=[N*i for i in range(1,11)]

with open('C:\python\ch12\Tables.txt','a') as f:
     f.write(str(table))
     f.write('\n')