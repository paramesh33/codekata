import math
a,b=input().split()
a=int(a)
b=int(b)
c=a*b
i=int(math.sqrt(c))
if(c==i*i):
    print('yes')
else:print('no')
