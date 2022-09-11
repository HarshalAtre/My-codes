a=54#Global variable
def func():
  global a#-->we command to use our global variable 'a',and dont create their own local variable 'a'
  print(a)
  a=8#Local variable 
  print(a)

func()
print(a)





