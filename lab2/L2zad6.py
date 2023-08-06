a= int(input("podaj 1 liczbe:"))
b=int(input("podaj 2 liczbe:"))
c=int(input("podaj 3 liczbe:"))
d=int(input("podaj 4 liczbe:"))
if a>b and a>c and a>d:
    print("najwieksza liczba:",a)
elif b>a and b>c and b>d:
    print("najwieksza liczba:", b)
elif c>a and c>b and c>d:
    print("najwieksza liczba:", c)
elif d>a and d>b and d>c:
    print("najwieksza liczba:", d)