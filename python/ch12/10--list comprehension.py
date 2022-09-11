a=[1,3,4,5,6,7,8,9,10]
# b=[]
# for item in a:
#   if item%2==0:
#    b.append(item)

# print(b)

'''A shortcut way to write it is'''
b=[i for i in a if i%2==0]
print(b)

t=[1,1,2,2,3,4,5,4,5,6]
s= {i for i in t }
print (s)#--> prints set of t






