x=int(input('Podaj liczbę'))
y=int(input('Podaj liczbę'))
z=int(input('Podaj liczbę, którą chcesz pierwiastkować'))

def suma(a,b):
    s=a+b
    return s

def roznica(a,b):
    r=a-b
    return r

def iloczyn(a,b):
    mnoz=a*b
    return mnoz

def iloraz(a,b):
    dzi=a/b
    return dzi
import math

def pierwiastkowanie(c):
    pier=math.sqrt(c)
    return pier
print(suma(x,y))
print(roznica(x,y))
print(iloczyn(x,y))
print(iloraz(x,y))
print(pierwiastkowanie(z))

