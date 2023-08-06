x=float(input("Na jakiej wysokości lecimy? [w metrach]:"))
def zaniskowysoko(wys):
    if wys<5:
        print(wys, "km to za nisko!")
    else:
        print("Na tej wysokości jesteś już bezpieczny")
print(zaniskowysoko(x))
