x = (int(input("Podaj liczbę naturalną:")))
while x>0:
    x = (int(input("Podaj liczbę naturalną:")))
    if x%12==0:
        print("Podałeś liczbępodzielną przez 12, wiec kończę działanie pętli")
        break
    else:
        continue