# censor 'donkey' word from a file

with open('C:\python\ch9\sample.txt','r') as f:
   a=f.read()

if 'donkey' in a :
    with open('C:\python\ch9\sample.txt','w') as f:
        f.write(a.replace('donkey','####'))
    




