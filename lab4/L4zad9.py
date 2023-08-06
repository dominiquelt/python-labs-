a=int(input('a= podaj liczbe calkowita:'))
b=int(input('b= podaj liczbe calkowita:'))
roznica=(a-b)
while abs(roznica)>=5:
    b=a
    print('teraz odjemnik=', a)
    a = int(input('a= podaj liczbe calkowita:'))
    roznica = (a - b)
print('wartosc bezwzgledna 2 kolejnych liczb jest mniejsza od 5, rowna:', abs(roznica))
print('a=',a, 'b=',b)
