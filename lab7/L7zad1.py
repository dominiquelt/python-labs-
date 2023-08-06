tuple1=(1,23,'kot',3,'krem','slon')

lenght=len(tuple1)
print(lenght,'dlugosc')

print(id(tuple1),'ID')

tuple2=tuple1+('pies',5)
print(id(tuple2),'ID2') #inny wynik
print(list(tuple2),'<---lista stworzona z drugiej krotki')
