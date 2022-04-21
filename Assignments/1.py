def Hz(line):
    for i in set(line):
        x = tuple(line).count(i)
        print(i,x)  
s1 = input("Enter string: ")
Hz(s1)