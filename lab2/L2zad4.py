x= int(input("podaj liczbe:"))
if x>0 and x%2==0:
    print("liczba jest dodatnia i poodzielna przez 2")
elif x>0 and x%2!=0:
    print("liczba jest dodatnia i niepodzielna przez 2")
elif x<0 and x%2==0:
    print("liczba jest ujemna i podzielna przez 2")
elif x<0 and x%2!=0:
    print("liczba jest ujemna i niepodzielna przez 2")
else:
    print("zero")