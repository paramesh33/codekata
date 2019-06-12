a=int(input())
n=a
res=0
while(n!=0):
    x=n%10
    res=(res*10)+x
    n=n//10
print(res)
