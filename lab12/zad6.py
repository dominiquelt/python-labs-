a=int(input('PODAJ LICZBĘ W SYSTEMIE DZIESIĘTNYM:'))
b=(input('PODAJ LICZBĘ W SYSTEMIE BINARNYM:'))

def dectobah(x):
    b=bin(x)
    h=hex(x)
    print("binarna:",b,"\nszesnastkowa:",h)

def bintohex(x):
    dec=int(x,2)
    h=hex(dec)
    return h

def hextobin(x):
    dec=int(x,16)
    b=bin(dec)
    return b

def bintohex(x):
    dec=int(x,2)
    h=hex(dec)
    return h

def bintohex(x):
    dec=int(x,2)
    h=hex(dec)
    return h
#przyklad z osemkowym

def bintohexandoct(x):
    dec=int(x,2)
    h=hex(dec)
    o=oct(dec)
    print("szesnastkowy",h,"\nosemkowy",o)


print(dectobah(a))
print(bintohex(b))
print(bintohexandoct(b))


