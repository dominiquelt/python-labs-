a=[]
i=1
y = (int(input("podaj liczbę całkowitą:")))
dzielenie=y%i
while i<y:
    if dzielenie==0:
        a.append(i)
    i+=1
    dzielenie = y % i
suma=sum(a)
print('suma dzielnikow calkowitych: ',suma)
if suma==y:
    print(y," to liczba doskonala!")
else:
    print(y, 'nie jest liczba doskonala')