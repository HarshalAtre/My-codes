b= set()
b.add(6)
b.add(46)
b.add(4)
b.add(96)
b.add(76)

# print(b)
# b.add({4:5}) not works as dictionaryand list are changable but tupple cant be changed
b.add((2,3))#works
print(b)
print(len(b))#prints length

b.remove(6)
print(b)
print(b.pop())
print(b)
print(b.union({4,6,7}))
print(b.intersection({67,4,88}))








