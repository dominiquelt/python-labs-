import random
ile=int(input('ile elementow ma byc w liscie?:'))
od=int(input('w zakresie od:'))
do=int(input('do:'))

list=[]
for i in range(1,ile+1):
    x=random.randint(od,do)
    list.append(x)
print(list)

nowa=[]
duplikaty=[]

for i in list:
    if i in nowa:
        duplikaty.append(i)
    else:
        nowa.append(i)
print('duplikaty:',duplikaty)

l=len(duplikaty)
for i in range(0,l-1):
    list.remove(duplikaty[i])

print('lista bez duplikatow',list)
dlugosc=len(list)
print('ostateczna dlugosc listy:',dlugosc)