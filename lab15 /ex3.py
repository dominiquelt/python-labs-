class Obywatel:
    def __init__(self):
        self.imie=''
        self.nazwisko=''
        self.ulica=''
        self.nr_domu=''
        self.kod_pocztowy=''
        self.miejscowosc=''
    def zapytanie(self):
        self.imie = input("Proszę podać imie")
        self.nazwisko = input("Proszę podać nazwisko")
        self.ulica = input("Proszę podać ulice")
        self.nr_domu = input("Proszę podać numer domu")
        self.kod_pocztowy = input("Proszę podać kod pocztowy")
        self.miejscowosc = input("Proszę podać miejscowosc")

    def wizytowka(self):
        return f"""Wizytowka:
        --------------------------
        {self.imie} {self.nazwisko}        
        {self.ulica} {self.nr_domu}
        {self.kod_pocztowy} {self.miejscowosc}
        --------------------------"""

def dopliku(nazwapliku,zawartosc):
    try:
       with open(nazwapliku,"w") as file:
           file.write(zawartosc)
       print("Wizytowka w pliku")
    except OSError:
        print("Błąd")

someone= Obywatel()
someone.zapytanie()
x=someone.wizytowka()
print(x)
dopliku("to.txt",x)

