a = int(input("podaj 1 liczbe:"))
b = int(input("podaj 2 liczbe:"))
c = int(input("podaj 3 liczbe:"))
if a > b and a > c:
    print("a wieksza")
elif b > c and b > a:
    print("b wieksza")
elif c > a and c > b:
    print("c wieksza")
elif a == b and b == c and c == a:
    print("podane liczby sa rowne")
