a=int(input())
n=a
c=1
while(n!=0):
    x=n%10
    c=c*x
    n=n//10
print(c)
