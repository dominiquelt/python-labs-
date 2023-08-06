A=["Real Madryt", "FC Barcelona", "Paris Saint-Germain", "Manchester United", "Juventus", "Chelsea", "Atletico Madrid", "Borussia Dortmund", "Liverpool", "Arsenal", "Inter Milan", "Manchester City", "AC Milan", "Roma", "Tottenham", "Schalke 04", "Olympique Lyonnais", "Valencia", "Sevilla", "Zenit St. Petersburg"]

import random
one=[]
two=[]
three=[]
four=[]

def uzupelnienia(lista,pula):
    b=[]
    while len(lista)<10:
        x=random.choice(pula)
        if x not in b:
            lista.append(x)
            b.append(x)
    p=set(lista)
    return p

x=uzupelnienia(one,A)  #set 1
y=uzupelnienia(two,A)  #set 2
z=uzupelnienia(three,A) #set 3
q=uzupelnienia(four,A)  #set 4
print('x:',x,'\ny:',y,'\nz:',z,'\nq:',q)

# intersection()
print('','\nczesc wspolna x i y',x.intersection(y))
print('czesc wspolna x i z',x.intersection(z))
print('czesc wspolna x i q',x.intersection(q))
#difference()
print('','\nróżnica zbiorów y i x',y.difference(x))
print('różnica zbiorów y i z',y.difference(z))
print('różnica zbiorów y i q',y.difference(q))
# union()
print('','\nsuma zbiorów z i x',z.union(x))
print('suma zbiorów z i y',z.union(y))
print('suma zbiorów z i q',z.union(q))

def dopelnienie(sset, pula=A):     #funkcja dopelniajaca 2 zestawy w celu ich powiekszenia,
    num = random.randint(0, 10)    #poniewaz do tej pory wszystkie mialy po 10 zespolow, a w nastepny liniach
    n = 0                          #zaprezentuje podzbiory
    while n < num:
        k = random.choice(pula)
        if k not in sset:
            sset.add(k)
        n += 1
    return sset

dq=dopelnienie(q)
dz=dopelnienie(z)
# issuperset()
print('','\nx jest podzbiorem dq:',dq.issuperset(x))
print('y jest podzbiorem dq:',dq.issuperset(y))
print('z jest podzbiorem dq:',dq.issuperset(z))

# issubset()
print('','\nx jest podzbiorem dz:',x.issubset(dz))
print('y jest podzbiorem dz:',x.issubset(dz))
print('z jest podzbiorem dz:',x.issubset(dz))

#dzięki tym funkcjom możemy odnaleźć informacje dotyczące relacji pomiędzy zbiorami








