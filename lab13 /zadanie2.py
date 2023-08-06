class ksiazka:
    def __init__(self, autor, tytul, okladka, strony, cena):
        self.autor=autor
        self.tytul=tytul
        self.okladka=okladka
        self.strony=strony
        self.cena=cena
    def czytaj(self):
        print("pozostało:", (self.strony-1))
    def udawajzeczytasz(self):
        print("Pretentious mode: ON")
    def dodajnotatki(self,):
        notatnik=[]
        x=input("Dopisz coś:")
        notatnik.append(x)
    def problem(self):
        if self.okladka != "twarda":
            print("Ta ksiazka predzej czy pozniej ulegnie destrukcji")
        else:
            print("Swietna okladka!")
    def coczytasz(self):
        return "Obecnie czytam {} autorstwa {}".format(self.tytul,self.autor)

portret=ksiazka("Oscar Wilde", "Portret Doriana Gray'a", 'miekka',240, 30)
interviews=ksiazka("David Foster Wallace", "Brief interviews with hideous men", 'miekka', 290, 60)
tumor=ksiazka("Stanisław Ignacy Witkiewicz","Tumor Mozgowicz",'miekka',35, 15)
pt=ksiazka("Adam Mickiewicz", 'Pan Tadeusz', 'twarda',344, 20)
alicja=ksiazka("Lewis Carroll","Alicja w Krainie Czarow",'twarda',100, 20)

print(alicja.coczytasz())
print(interviews.udawajzeczytasz())
print(interviews.problem())
print(pt.problem())
print(portret.dodajnotatki())