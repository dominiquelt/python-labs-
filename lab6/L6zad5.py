n=int(input('ile liczb chcesz wygenerowac?:'))
x=int(input('w zakresie od:'))
z=int(input('do:'))
a=[]
i=1
for element in range(x,z+1):    #petla na liste
    if i>n:
        break
    a.append(element)
    i+=1
print('wygenerowano:',a)
print('usunieto 3-eci element od konca:',a[-3])
trzeci=a.pop(-3)
print(a)
k=int(input('ktory jeszcze element od konca chcesz usunac?:'))
print('usunieto',k,'element od konca:',a[-k])
ka=a.pop(-k)
print(a)

print('drugi ciag:')
m=int(input('ile liczb chcesz wygenerowac?:')) #2petla
o=int(input('w zakresie od:'))
p=int(input('do:'))
b=[]
i=1
for element in range(o,p+1):
    if i>m:
        break
    b.append(element)
    i+=1
print('wygenerowano:',b)

c=a+b
powtorzenia=[]
print(c)
for i in a:
     if i in b:
         x=powtorzenia.append(i)
print('te liczby sie powtarzaja',powtorzenia,)
l=len(c)
dd=len(powtorzenia)
d=0
while d<dd:
    ile= c.count(powtorzenia[d])
    print('w scalonej liscie',powtorzenia[d],'wystepuje',ile,'razy')
    d+=1


