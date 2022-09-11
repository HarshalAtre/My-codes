with open("C:\python\ch9\log.txt",'r') as f:
    a=f.read().lower()#lower() converts PYTHON in python (inlower case) to detect word written in any case
    if 'python' in a:
     print('Yes, file contains the word python')
    else:
        print("No, file doesn't contains the word python ")






