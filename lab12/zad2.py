import math
def kulapole(r):
    polekuli=4*(math.pi)*r
    return polekuli
print("POLE KULI: ", kulapole(1))

def kulavolume(r):
    kulav= (4/3)*(math.pi)*r
    return kulav
print("OBJĘTOŚĆ KULI: ", kulavolume(1))

def stozekpole(r,l):
    stpole=((math.pi)*r*(r+l))
    return stpole
print("POlE STOŻKA: ", stozekpole(1,2))

def stozekvolume(r,h):
    stvolume=((math.pi)*h*r**2)/3
    return stvolume
print("OBJĘTNOŚĆ STOŻKA", stozekvolume(1,2))

def szescianpole(a):
    szpole=6*a**2
    return szpole
print("POLE SZESCIANU: ", (szescianpole(1)))

def szescianvolume(a):
    szvolume=a**3
    return szvolume
print('OBJETOSC SZESCIANU', szescianvolume(1))