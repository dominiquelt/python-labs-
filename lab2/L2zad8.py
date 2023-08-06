a= float(input("podaj długość przeciwprostokątnej  a:"))
b= float(input("podaj długość przyprostokątnej b:"))
c= float(input("podaj długość przyprostokątnej c:"))
trojkat_prostokatny= a**2==b**2 + c**2
if a>b and a>c:
    print("sprawdzam czy trójkąt jest prostokątny:")
if trojkat_prostokatny:
    print("TRÓJKAT JEST PROSTOKĄTNY!!!")
else:
    print("TRÓJKĄT NIE JEST PROSTOKĄTNY:(")

