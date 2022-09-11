from random import uniform


class emp:
    com="yahoo"
    uniform="blue"
    

nick=emp()
soham=emp()
naman=emp()
naman.uniform="red"# checks first here then in class.


print(nick.uniform)
print(soham.uniform)
print(naman.uniform)