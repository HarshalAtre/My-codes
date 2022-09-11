from ntpath import join
import random
import string

p1=list(string.ascii_lowercase)

p2=list(string.ascii_uppercase)

p3=list(string.digits)

p4=list(string.punctuation)

p=p1+p2+p3+p4

random.shuffle(p)

user=int(input("Enter the password characters range\n Remember more the characers the more the password is. : "))

password=''.join(p[0:user])

print(password + '   <-- Select and right click to copy')