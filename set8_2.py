s=input()
d=0
for x in s:
    if(x=='a'or x=='A'or x=='e'or x=='E'or x=='i'or x=='I'or x=='o'or x=='O'or x=='u'or x=='U'):
        d=d+1
if d==0:print('no')
else:print('yes')
