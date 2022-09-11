import os


with open('C:\python\ch9\python.txt') as f:
    a=f.read()
    with open('C:\python\ch9\Renamed_by_python','w') as d:
     d.write(a)


os.remove('C:\python\ch9\python.txt')
