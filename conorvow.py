a=input()
a=ord(a)
if ((a>=65&a<=90)or(a>=97&a<=122)):
    if a==65 or a==69 or a==73 or a==79 or a==85 or a==97 or a==101 or a==105 or a==111 or a==117:
        print('Vowel')
    else:print('Consonant') 
else:print('Invalid')
