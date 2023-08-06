print('WITAM W miniLOTTO!')
numbers=[]
for i in range(1,50):   #tablica do losowania na pozniej
    numbers.append(i)
y=""
ticket=[]  #los
bin=[]
for i in range(1,6):
    y = int(input('Skresl liczbe od 1 do 42: '))
    while y > 42 or y < 1 or y in bin:
        print('System przyjmuje jedynie liczby od 1 do 42','ponadto kazda liczbe mozna wpisac tylko raz', sep='\n')
        y = int(input('podaj inna:'))
    ticket.append(y)
    bin.append(y)
print('oto twoj los: ', ticket, sep='\n')
wynik=[]
import random
for i in range(1,6):
    wybor = random.choice(numbers)
    wynik.append(wybor)
    numbers.remove(wybor)
print('wyniki losowania lotto:',wynik, sep="\n")

n=len(ticket)
compare=[]
i=0
while i<=n-1:
    if ticket[i] in wynik:
        compare.append(ticket[i])
    i+=1
print('liczby pokrywajace sie z wynikiem losowania',compare, sep='\n')
ile=len(compare)
while ile>2:
    print('TRAFIONO ',ile,' ZE SKRESLONYCH 5 LICZB','odbierz nagrode w punkcie',sep="\n")
