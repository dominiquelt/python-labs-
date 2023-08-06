x=int(input('podaj liczbe naturalna:'))
dzielniki=[]
for i in range(1,x+1):
    if x%i==0:
        dzielniki.append(i)
print('oto dzielniki',dzielniki)