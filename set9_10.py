a=input()
if a.isalnum():
    for x in a:
        if x.isdigit():
            print(x,end='')
else:print('')
