a=int(input())
n,count=a,0
while(n!=1):
    n=n/2
    count=count+1
print(2**(count+1))
