a=0
b=1
c=0
while not c > 0:
    c=a+b
    a=0
    b=c
    print(a,b, end=',')
while not c > 22:
    c=a+b
    a=b
    b=c
    print(c, end=',')
   