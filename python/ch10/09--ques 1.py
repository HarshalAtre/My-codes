from socket import NI_DGRAM


class programmer:
    company="microsoft"
    uniform='blue'
    
    def __init__(self,name):
        self.name=name
har=programmer('harshal')
nick=programmer('nikhil')

print(har.company)
print(nick.company)
print(har.uniform)
print(nick.uniform)
print(har.name)
print(nick.name)





