print('WITAM W LOTTO!')
numbers=[]
for i in range(1,50):   #tablica do losowania na pozniej
    numbers.append(i)
y=""
ticket=[]  #los
bin=[]
for i in range(1,7):
    y = int(input('Skresl liczbe od 1 do 49: '))
    while y > 49 or y < 1 or y in bin:
        print('System przyjmuje jedynie liczby od 1 do 49','ponadto kazda liczbe mozna wpisac tylko raz', sep='\n')
        y = int(input('podaj inna:'))
    ticket.append(y)
    bin.append(y)

print('oto twoj los: ', ticket, sep='\n')
wynik=[]
import random
for i in range(1,7):
    wybor = random.choice(numbers)
    wynik.append(wybor)
    numbers.remove(wybor)
print('wyniki losowania lotto:',wynik, sep="\n")
if ticket==wynik:
    print('zostala/es milionerem!!!!')
else:
    print('try your luck some other time:/')


