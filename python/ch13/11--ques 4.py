l=[5,10,30,34,35,36,38,22,4]

def div_by_5(num):
    if(num%5==0):
        return True
    else:    
        return False

print(list(filter(div_by_5,l)))







