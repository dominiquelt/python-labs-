krotka=('kot','stol','pies','mysz','sufit','krzeslo')
p= 'kot' in krotka
print(p,'jest')
i=krotka.index('kot')
print(i,'indeks dla kot')
nowe=('ala ma kot',)
x=krotka+nowe
z= 'kot' in x
print(z)
print(x) #tupla po dodaniu
lista=list(x) #nowa tupla na liste
podz=[]
for i in x:
    if " " in i:
       i= i.split()
       for elements in i:
           podz.append(elements)
    else:
        podz.append(i)
ost=tuple(podz)
print(ost)
ile=ost.count('kot')
print(ile)

