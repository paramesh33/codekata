a=input()
c=list(a)
b=len(a)
for x in range(b):
    if x%2==0:
        print(c[x],end='')
print(end=' ')
for x in range(b):
    if x%2!=0:
        print(c[x],end='')
