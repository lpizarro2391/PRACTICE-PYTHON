a=int(input("indique el primer numero :"))
b=int(input("indique el segundo numero :"))
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
   