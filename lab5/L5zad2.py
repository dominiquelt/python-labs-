n=int(input('6 liczb w zakresie od:'))
x=int(input('do:'))
a=[]
i=1
for elements in range(n,x):
    if i>6:
        break
    a.append(elements)
    i+=1
print(a)
min=min(a)
max=max(a)
aa=sorted(a)
mediana= (a[2]+a[3])/2
srednia= sum(a)/6
print('minimum=',min,'\nmaximum=',max,'\nmediana=',mediana,'\nsrednia=',srednia,)
