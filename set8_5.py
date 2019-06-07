a=input()
b=len(a)
d=list(a)
if b%2==0:
    c=b//2
    for x in d:
        if d[c]==x or d[c-1]==x:
            print('*',end='')
        else:
             print(x,end='')   
else:
    for x in d:
        c=b//2
        if d[c]==x:
            print('*',end='')
        else:
             print(x,end='')
