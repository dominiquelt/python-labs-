menu={'zupa1':10, 'zupa2':11, 'zupa3':12,'danie1':30,'danie2':33,'danie4':35,'deser1':22,'deser2':28,'deser3':50}
for i in menu.keys():
    print(i)
for i in menu.values():
    print(i)
for y,z in menu.items():
    print(y,z)

print(max(menu.values()))
print(min(menu.values()))

print(menu)


del menu['zupa1']
del menu['deser3']
print(menu)

print('dodaj element')
n=(input('podaj nazwe dania:'))
c=float(input('podaj cene dania:') )
menu['n']=c
print(menu)