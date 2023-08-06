numbers=[]
for i in range(1,81):   #tablica do losowania na pozniej
    numbers.append(i)
print('OTO MULTIMULTI')
#sekcja wyboru
x=int(input('Podaj liczbe skreslen od 1 do 10:'))
while x > 10 or x< 1 :
    print('ilosc skreslen musi znalezc sie w przedziale 1-10')
    x = int(input('podaj inna:'))
a=[]
bin=[]
n=x
for i in range(1,(n+1)):
    y=int(input('Skresl liczbe (1-80):'))
    while y>80 or y<1 or y in bin:
        print('System przyjmuje jedynie liczby od 1 do 49', 'ponadto kazda liczbe mozna wpisac tylko raz', sep='\n')
        y = int(input('podaj inna:'))
    a.append(y)
    bin.append(y)
print('twoj los:',a)

#losowanie
wynik=[]
import random
for i in range(1,21):
    wybor = random.choice(numbers)
    wynik.append(wybor)
    numbers.remove(wybor)
print('wyniki losowania multimulti:',wynik, sep="\n")
#wynik podajacego
n=len(a)
compare=[]
i=0
while i<=n-1:
    if a[i] in wynik:
        compare.append(a[i])
    i+=1
print('liczby pokrywajace sie z wynikiem losowania',compare, sep='\n')
ile=len(compare)
print('TRAFIONO ',ile,' ZE SKRESLONYCH',x,'LICZB')





