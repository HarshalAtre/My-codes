def per(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
    return p

marks1=[78,89,68,60]
perc1=per(marks1)

marks2=[79,64,68,89]
perc2=per(marks2)

print(perc1,perc2)

