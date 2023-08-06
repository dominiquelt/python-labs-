wysokosc= int(input("na jakiej wysokości lecimy?(w metrach): "))
minwysokosc = 5000

if wysokosc<min_wysokosc:
    print(str(wysokosc/1000) + "km to za nisko!")
else:
    print("Na tej wysokości jesteś już bezpieczny")