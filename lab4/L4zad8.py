i=1
x=333
y=0
while i<=12:
    y=y+x
    y=(float(y+(float(y*(8/100)))))
    i+=1
    print(y)
    if i==12:
        print("wynik końcowy:")