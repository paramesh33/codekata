a,b=input().split()
a=int(a)
b=int(b)
for x in range(a+1,b):
    if x%2!=0:
        print(x,end=' ')
