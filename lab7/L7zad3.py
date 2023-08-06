a=[]
for i in range (2,202,2):
    a.append(i)
tu1=tuple(a)
print(tu1)
b=[]
for i in range(1,200,2):
    b.append(i)
tu2=tuple(b)
print(tu2)
tuple=tu1+tu2
print(tuple)
zero=tuple.count(0)
print('zero wystepuje',zero,'razy')
sto=tuple.count(100)
print('100 wystepuje',sto,'raz')
print(id(tu1),'tuple1 ID')
print(id(tu2),'tuple2 ID')
print(id(tuple),'polaczona ID')
