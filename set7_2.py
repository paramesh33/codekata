def check(string): 
    p=set(string)
    s={'0','1'}
    if s==p or s=={'0'} or p=={'1'}:
        print('yes')
    else:print('no')
s=input()
check(s)
