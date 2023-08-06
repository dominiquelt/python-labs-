import random
a=['orzel','reszka']
orly=[]
reszki=[]
for i in range (1,51):
    wynik=random.choice(a)
    if wynik=='orzel':
        orly.append(wynik)
    else:
        reszki.append(wynik)
x=len(orly)
y=len(reszki)
roznica=abs(x-y)
if x>y:
    print('orlow wylosowano:',x, '\nreszek wylosowano:',y,'\norlow o',roznica,'wiecej')
elif y>x:
    print('orlow wylosowano:',x, '\nreszek wylosowano:',y,'\nreszek o',roznica,'wiecej')
else:
    print('wylosowano tyle samo orlow co reszek')
