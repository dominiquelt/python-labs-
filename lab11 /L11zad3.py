import math
stopnie = float(input("Podaj wartość kąta w stopniach np. 70, 90, 35, 180, 240, 360: "))
radiany = math.radians(stopnie)

try:
    sin = math.sin(radiany)
    print("sin({}) = {}".format(stopnie, sin))
except ValueError:
    print("sin({}) nie ma wartości".format(stopnie))

try:
    cos = math.cos(radiany)
    print("cos({}) = {}".format(stopnie, cos))
except ValueError:
    print("cos({}) nie ma wartości".format(stopnie))

try:
    tan = math.tan(radiany)
    print("tan({}) = {}".format(stopnie, tan))
except ValueError:
    print("tan({}) nie ma wartości".format(stopnie))

try:
    ctan = 1 / tan
    print("ctan({}) = {}".format(stopnie, ctan))
except (ValueError, ZeroDivisionError):
    print("ctan({}) nie ma wartości".format(stopnie))