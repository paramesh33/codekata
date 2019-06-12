a,b=map(int,input().split())
c=list(map(int,input().split()))
d=[]
for x in range(a):
    if c[x]%2==0:
        pass
    else:
        d.append(c[x])
print(d[b-1])
