a=[]
i=1
y = (int(input("podaj liczbę całkowitą:")))
dzielenie=y%i
while i<=y:
    if dzielenie==0:
        a.append(i)
    i+=1
    dzielenie = y % i
ilosc= len(a)
if ilosc==2:
    print(a)
    print('podana liczba jest liczba pierwsza')
else:
    print(a, 'you wish')
