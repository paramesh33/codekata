a,b=input().split()
a=int(a)
b=int(b)
c=list(map(int,input().split()))
d=0
for x in range(b):
    d=d+c[x]
print(d)
