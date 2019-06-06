a=int(input())
n=a
c=0
while(n!=0):
    b = n%10
    c = c*10 + b
    n=n//10
if c==a:
    print('yes')
else:print('no')
