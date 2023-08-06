x=input('podaj liczbe calkowita:')
n=[]
rn=[]
for element in x:
    n.append(element)
l=len(n)
i=-1
while i>=-l:
    rev=n[i]
    rn.append(rev)
    i-=1
odwr=''
for element in rn:
    odwr=odwr+element
    
if n==rn:
    print('wczytana liczba jest palindromem!','spojrz:',x,odwr,sep='\n')
else:
    print('twoja liczba-odwrocona:',odwr,sep='\n')
