import random
a=[0,1]
one=[]
zero=[]
for i in range (1,51):
    wynik=random.choice(a)
    if wynik==0:
        zero.append(wynik)
    else:
        one.append(wynik)
x=len(one)
y=len(zero)
roznica=abs(x-y)
if x>y:
    print('jednynek wylosowano:',x, '\nzer wylosowano:',y,'\njedynek o',roznica,'wiecej')
elif y>x:
    print('jednynek wylosowano:',x, '\nzer wylosowano:',y,'\nzer o',roznica,'wiecej')
else:
    print('wylosowano tyle samo jedynek co zer')
