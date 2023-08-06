A=["Real Madryt", "FC Barcelona", "Paris Saint-Germain", "Manchester United", "Juventus", "Chelsea", "Atletico Madrid", "Borussia Dortmund", "Liverpool", "Arsenal", "Inter Milan", "Manchester City", "AC Milan", "Roma", "Tottenham", "Schalke 04", "Olympique Lyonnais", "Valencia", "Sevilla", "Zenit St. Petersburg"]

import random
one=[]
two=[]
three=[]
four=[]

def uzupelnienia(lista,pula=A):
    b=[]
    while len(lista)<10:
        x=random.choice(pula)
        if x not in b:
            lista.append(x)
            b.append(x)
    p=set(lista)
    return p

x=uzupelnienia(one,)
y=uzupelnienia(two,)
z=uzupelnienia(three,)
q=uzupelnienia(four,)

def dopelnienie(sset, pula=A):
    num = random.randint(0, 10)
    n = 0
    while n < num:
        k = random.choice(pula)
        if k not in sset:
            sset.add(k)
        n += 1
    return sset

dq=dopelnienie(q,)
dz=dopelnienie(z,)
dy=dopelnienie(y,)
dx=dopelnienie(x,)
print('\ndx:',dx,'\ndy:',dy,'\ndz:',dz,'\ndq:',dq, end='\n')
print(len(dx),'dlugosc dx', end=' \n')
print(len(dy),'dlugosc dy', end=' \n')
print(len(dz),'dlugosc dz', end=' \n')
print(len(dq),'dlugosc dq', end=' \n')

def usuwanie(zbior,):
    U=["AC Milan", "Roma", "Tottenham", "Schalke 04"]  #przykladowe zespoly do usuniecia
    for i in U:
        if i in zbior:
            zbior.remove(i)
    return zbior

udx=usuwanie(dx)
udy=usuwanie(dy)
udz=usuwanie(dz)
udq=usuwanie(dq)

print('\nudx:',udx,'\nudy:',udy,'\nudz:',udz,'\nudq:',udq)
print(len(udx),'dlugosc udx', end=' \n')
print(len(udy),'dlugosc udy', end=' \n')
print(len(udz),'dlugosc udz', end=' \n')
print(len(udq),'dlugosc udq', end=' \n')

porownanie1= udx.issubset(dx)
print(porownanie1)         #porownanie

listaa=list(udx)   #konwersja
print(listaa)
