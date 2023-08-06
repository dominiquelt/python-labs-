print('WITAM W LOTTO!')
numbers=[]
for i in range(1,50):   #tablica do losowania na pozniej
    numbers.append(i)
y=""
ticket=[]  #los
i=1

while i<=6:
    y = int(input('Skresl liczbe od 1 do 49: '))
    if y in ticket:
        print('ta liczba zostala juz skreslona!')
        y=int(input('Skresl inna liczbe od 1 do 49:'))
        ticket.append(y)
        i += 1
    elif y>49:
        print('mozesz skreslic liczby w przedziale od 1 do 49')
        y = int(input('Skresl inna liczbe od 1 do 49:'))
        ticket.append(y)
        i += 1
    elif y<1:
        print('mozesz skreslic liczby w przedziale od 1 do 49')
        y = int(input('Skresl inna liczbe od 1 do 49:'))
        ticket.append(y)
        i += 1
    else:
        ticket.append(y)
        i+=1

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









