def czytokod(kod):
    if len(kod) != 6:
        raise ValueError("dlugosc kodu inna niz przewidywana")
    elif not kod[:2].isdigit():
        raise ValueError("niewlasciwy ciag liczb")
    elif kod[2] != "-":
        raise ValueError("niewlasciwy ciag liczb")
    elif not kod[3:].isdigit():
        raise ValueError("niewlasciwy ciag liczb")
    else:
        with open('kody_pocztowe.txt','a') as file:
            file.write(kod + "\n")
        print("kod dodany do listy")

try:
    kodinput=input("prosze o podanie kodu:")
    czytokod(kodinput)
except ValueError as e:
    print(e)


