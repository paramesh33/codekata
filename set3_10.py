a,b=input().split()
c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if c>a:
    if b>d:
        d=d+60
        e=d-b
        f=c-(a+1)
    else:
        e=d-b
        f=c-a
else:
    if b<d:
        b=b+60
        e=b-d
        f=a-(c+1)
    else:
        e=b-d
        f=a-c
print(f,e)
