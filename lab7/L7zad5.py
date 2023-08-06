krotka=('dzielenia',)
tupla=('niedziela',)
lista1=[]
lista2=[]
for elements in krotka:
    x=list(elements)
    print(x)
for elements in tupla:
    z=list(elements)
    print(z)
j=sorted(x)
d=sorted(z)
if j==d:
    print('moze byc anagram')