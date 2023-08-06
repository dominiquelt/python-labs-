a=[]
for i in range(0,101):
    a.append(i)
sum=0
for i in a:
    szescian=a[i]**3
    sum+=szescian
    if sum>10**6:
        break
print('nalezy zsumowac',i+1,'liczb naturalnych zaczynajac od 0')
print('suma=',sum,' > ',10**6)
