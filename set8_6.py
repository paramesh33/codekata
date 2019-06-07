a=int(input())
d=0
for x in range(2,a//2):
    if a%x==0:
        d=1
if d==0:
    print('no')
else:print('yes')
