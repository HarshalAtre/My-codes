def sq(num):
    return num*num

l=[1,2,4]    
#  Method 1
l2=[]
for item in l:
    l2.append(sq(item))
    
print(l2)

# Method 2 --->map function

print(list(map(sq,l)))






