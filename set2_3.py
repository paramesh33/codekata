a=int(input())
n=a//2
d=0
for x in range(2,n+1):
    if a%x==0:
        d=1 
if d==0:
    print('yes')
else:print('no')
