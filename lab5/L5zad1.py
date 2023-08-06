x=int(input('podaj ilosc liczb do wprowadzenia:'))
i=1
sum=0
while i<=x:
    y=float(input("wprowadz liczbe:"))
    if y<0:
        print('system przyjmuje jedynie liczby nieujemne')
        continue
    sum+=y
    i+=1
arytmetyczna=sum/x
print('oto szukana srednia arytmetyczna',arytmetyczna)