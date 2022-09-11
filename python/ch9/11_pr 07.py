a=True
i=1
with open("C:\python\ch9\log.txt",'r') as f:
   
   while a:
    a=f.readline().lower()
    if "python" in a:
         print(f'python word is present in {i} line')
    i+=1






