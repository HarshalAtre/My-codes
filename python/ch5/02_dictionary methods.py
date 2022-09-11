mydict={
    "fast" : "in quick manner",
    "harry" : "a coder",
    "marks":[1,2],
    }

print(mydict.keys())
print(type(mydict.keys()))
print(list(mydict.keys()))
print(type(mydict.keys()))

print(mydict.values())

print(mydict.items())

print(mydict.get("fast"))



print(mydict)
updict={"jee": "hard"}
mydict.update(updict)
print(mydict)

print(mydict.get("fas"))#prints none if not available in dictionary



