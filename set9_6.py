s=input()
b=[]
d=0
for x in s:
    if x in b:
        d=d+1 
    else:
        b.append(x)
if d==0:
    print('Yes')
else:print('No')
