a=[]
for i in range(0,101):
    a.append(i)
sum=0
for i in a:
    szescian=a[i]**3
    sum+=szescian
print('suma szescianow liczb od 0 do 100=',sum)