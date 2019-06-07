a=input()
b=len(a)
d=list(a)
if b%2==0:
    c=b//2
    for x in range(b):
        if x==c or x==c-1:
            print('*',end='')
        else:print(d[x],end='')
else:
    for x in range(b):
        c=b//2
        if x==c:
            print('*',end='')
        else:
             print(d[x],end='')
