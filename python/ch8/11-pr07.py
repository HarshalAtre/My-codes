def remove_and_split(string, word):
     newstr=string.replace(word, "")
     return newstr.strip()

a="       harry is good      "
b=remove_and_split(a,"harry")

print(b)