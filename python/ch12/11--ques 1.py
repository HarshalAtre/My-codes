def read(Name):
    try:
        with open(f'C:\python\ch12\{Name}','r') as f:
            print(f.read())
    except FileNotFoundError:
            print(f'{Name} file not found')

read("1.txt")
read("2.txt")
read("3.txt")
read("m.txt")








