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
print(x,y,z,q,sep='\n')






