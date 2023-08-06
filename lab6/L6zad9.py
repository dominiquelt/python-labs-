n=int(input('ile elementow ma zawierac lista?;'))
a=[]
for i in range(n):
    x=int(input('Dodaj do listy liczbe calkowita:'))
    a.append(x)
print(a)
m=max(a)
count=a.count(m)
print("najwiekszy element",m,'wystapil w liscie',count,'razy')
