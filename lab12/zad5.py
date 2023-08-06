a=float(input("Podaj swoja wage w kg"))
b=float(input("Podaj swoj wzrost w metrach"))

def BMI(masa,wzrost):
    b = (masa)/(wzrost*wzrost)
    if b<=18.5:
        print("niedowaga")
    elif 18.5<b<=24.99:
        print("waga jest prawidłowa")
    else:
        print("nadwaga")

print(BMI(a,b))