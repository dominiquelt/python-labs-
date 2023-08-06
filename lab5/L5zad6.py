print('ZA DUZO, ZA MALO')
a=[]
for i in range(0,101):
    a.append(i)
import random
magicnumber=random.choice(a)
for i in range(1,4):
    x=int(input('sprobuj odgadnac magiczna liczbe w zakresie (1-100):'))
    if x==magicnumber:
        print("Gratulacje!")
        break
    elif x<magicnumber:
        print('Podales za mala wartosc.')
    elif x>magicnumber:
        print('Podales za duza wartosc.')
if x!=magicnumber:
    print('Haha, przegrales')
print('Magiczna liczba to:',magicnumber)
