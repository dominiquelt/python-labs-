imie= input("Podaj swoje imię: ")
nazwisko= input("Podaj swoje nazwisko: ")
tel= input("Podaj (proszę) swoj numer telefonu: ")
but=input("Podaj swoj rozmiar buta ")

imie_litery= imie.isalpha()
nazwisko_litery= nazwisko.isalpha()

tel_cyfry= tel.isdigit() #sprawdzanie czy nr buta i telefonu to cyfry
but_cyfry= but.isdigit()

imie= imie.capitalize()
nazwisko= nazwisko.capitalize()

tel =tel.replace("-","").replace(" ", "")
but =but.replace("-","").replace(" ", "")

kobieta = False  #plec
if imie[-1] == "a":
  kobieta= True

print(f"Imię i nazwisko składają się TYLKO z liter: {imie_litery and nazwisko_litery}")
print(f"Numerr telefonu i numer buta składają się TYLKO z cyfr: {tel_cyfry and but_cyfry}")
print(f"IMIE I NAZWISKO Z dużej LITERY: {imie} {nazwisko}")
print(f"Numer telefonu po usunięciu znaków: {tel}")
print(f"Rozmiar buta po usunięciu znaków: {but}")
print(f"Użytkownik jest kobietą: {kobieta}")
