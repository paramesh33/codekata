a=int(input())
b=list(map(int,input().split()))
for x in range(a):
    if b[x]>b[x+1]:
        print(x)
        break
