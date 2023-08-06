class zwierze:
    def __init__(self,gatunek,konczyny,czy_domowe,dzwiek):
        self.gatunek=gatunek
        self.konczyny=konczyny
        self.czy_domowe=czy_domowe
        self.dzwiek=dzwiek
    def dajglos(self):
        return "{}".format(self.dzwiek)
    def coto(self):
        return "Jestem {}".format(self.gatunek)
    def czy_mozna_miec_w_domu(self):
        if self.czy_domowe == "tak":
            print("Jestem domownikiem!")
        else:
            print("Zostaw mnie w spokoju!!!")
    def ile_konczyn(self):
        return "mam {} konczyn/y".format(self.konczyny)

class kot(zwierze):
    def __init__(self, imie, rodzaj):
        super().__init__("ssak", 4, "tak", "Meow!")
        self.imie=imie
        self.rodzaj=rodzaj
    def przedstawienie(self):
        return "Mam na imie {}, jestem {},{}".format(self.imie,self.gatunek,self.rodzaj)



class pies(zwierze):
    def __init__(self, imie, rodzaj):
        super().__init__("ssak", 4, "tak", "Woof WOOF!")
        self.imie=imie
        self.rodzaj = rodzaj
    def przedstawienie(self):
        return "Mam na imie {}, jestem {},{}".format(self.imie,self.gatunek,self.rodzaj)



class ptak(zwierze):
    def __init__(self, imie, rodzaj):
        super().__init__("ptak", 2, "tak", "Chirp,chirp..")
        self.imie=imie
        self.rodzaj = rodzaj
    def przedstawienie(self):
        return "Mam na imie {}, jestem {},{}".format(self.imie,self.gatunek,self.rodzaj)


class ryba(zwierze):
    def __init__(self, imie,rodzaj):
        super().__init__("ryba", 0, "tak", "Bulbulbulbulbulbulbulbulbulbul...")
        self.imie=imie
        self.rodzaj = rodzaj
    def przedstawienie(self):
        return "Mam na imie {}, jestem {},{}".format(self.imie,self.gatunek,self.rodzaj)

ryyba=ryba("nemo","błazenek")
piess=pies("burek","pies beagle")
kott=kot("shila","kot brytyjski")
ptakk=ptak("hugo","koliber")

print(ryyba.przedstawienie())
print(ptakk.przedstawienie())
print(kott.przedstawienie())
print(piess.przedstawienie())

