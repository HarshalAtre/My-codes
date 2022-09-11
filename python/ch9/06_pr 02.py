def game():
    return 45

score=game()
# print(type(score))


f=open('C:\python\ch9\hiscore.txt','r')



hiscore=int(f.read())
hiscore=int(hiscore)
while hiscore>score:
 if hiscore>score:
    break
d=open('C:\python\ch9\hiscore.txt','w')
f.close()
if hiscore<score:
    d.write(str(score))



if hiscore>score:
    d.write(str(hiscore))
d.close()


