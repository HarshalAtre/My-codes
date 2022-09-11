
# censor list from a file
b=['donkey','pumpkin','pot']
with open('C:\python\ch9\sample.txt','r') as f:
   a=f.read()

for word in b:
    a=a.replace(word,'####')
    with open('C:\python\ch9\sample.txt','w') as f:
        f.write(a)
    

