a=input()
b=[int(x) for x in str(a)]
for x in b:
    if x%2!=0:
        print(x,end=' ')
