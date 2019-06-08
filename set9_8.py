a,b=input().split()
a=int(a)
b=int(b)
if a>b:
    num=a
    denom=b
else:
    num=b
    denom=a
rem=num%denom
while(rem!=0):
    num=denom
    denom=rem
    rem=num%denom
print(int((a*b)/denom))
