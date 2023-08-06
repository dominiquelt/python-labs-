import random
t=[]
for i in range(1,101):
    x=random.choice(range(0,11))
    t.append(x)
tupla=tuple(t)
print(tupla)
zero=tupla.count(0)
one=tupla.count(1)
two=tupla.count(2)
print('zera:',zero,'\njedynki:',one,'\ndwojki:',two)