print("to jest równanie kwadratowe: ax**2 + bx + c")
a = float(input("podaj zmienna 'a':"))
b = float(input("podaj zmienna 'b':"))
c = float(input("podaj zmienna 'c': "))
print("obliczam delte:")
delta = (b**2)-(4*a*c)
print("TO JEST DELTA:", delta)
import math
duo= delta**1/2
x1= (-b + duo )/2*a
x2= (-b - duo)/2*a
x0= (-b)/2*a
if delta<0.0:
   print("brak rozwiazan")
elif delta>0:
   print("x1", x1)
   print("x2", x2)
else:
   print("x0:", x0)