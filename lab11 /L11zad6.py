print("wybierz jedna zamiane")
print("1: zamiana liczby dziesiętnej na binarną")
print("2: zamiana liczby dziesiętnej na ósemkową")
print("3: zamiana liczby dziesiętnej na szesnastkową")
print("4: zamiana liczby binarnej na dziesiętną")
print("5: zamiana liczby ósemkowej na dziesiętną")
print("6: zamiana liczby szesnastkowej na dziesiętną")

wybrano = int(input("Wprowadź swój wybór: "))
if wybrano == 1:
    dziesietna = int(input("podaj liczbę dziesiętną: "))
    dziesietne_binarne = int(bin(dziesietna).replace("0b", ""))
    print("wynik:", dziesietne_binarne)
elif wybrano == 2:
    dziesietna = int(input("podaj liczbę dziesiętną: "))
    dziesietne_osemkowe = oct(dziesietna).replace("0o", "")
    print("wynik:", dziesietne_osemkowe)
elif wybrano == 3:
    dziesietna = int(input("podaj liczbę dziesiętną: "))
    dziesietne_szesnatkowe = hex(dziesietna).replace("0x", "")
    print("wynik:", dziesietne_szesnatkowe)
elif wybrano == 4:
    binarna = input("podaj liczbę binarną: ")
    binarne_dziesietne = int(binarna, 2)
    print("wynik:", binarne_dziesietne)
elif wybrano == 5:
    osemkowa = input("podaj liczbę ósemkową: ")
    osemkowe_dziesietne = int(osemkowa, 8)
    print("wynik:", osemkowe_dziesietne)
elif wybrano == 6:
    szesnastkowa = input("podaj liczbę szesnastkową: ")
    szesnatkowe_dziesietne = int(szesnastkowa, 16)
    print("wynik:", szesnatkowe_dziesietne)

print('PROSZE BARDZO!')
