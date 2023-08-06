class smartfon:
    def __init__(self, marka, model, kolor, pamiec, bateriateraz, obudowa, szklo):
        self.marka=marka
        self.model=model
        self.kolor=kolor
        self.pamiec=pamiec
        self.bateriateraz=bateriateraz
        self.obudowa=obudowa
        self.szklo=szklo
    def klikaj(self):
        print("KLIK-KLIK")
    def doomscrolling(self):
        self.bateriateraz -=1
        print("produktywnosc=0")
    def zamalopamieci(self, pamieczajeta):
        if pamieczajeta >= (0.75 * self.pamiec):
            print("Powoli brakuje miejsca")

    def stanbaterii(self):
        if self.bateriateraz <= 20:
            print(" Niski stan baterii!")

    def case(self):
        if self.obudowa == "brak":
            print("prosze zakupic obudowe")
    def szkloo(self, pekniecie):
        if self.szklo == "brak":
            print("prosze zakupic szklo")
        elif pekniecie >=2:
            print("prosze zakupic nowe szklo")

ip=smartfon('Apple',"Iphone 13","czarny",128, 58, "brak", "jest")

print(ip.doomscrolling())
print(ip.case())
print(ip.szkloo(4))
print(ip.stanbaterii())
print(ip.zamalopamieci(120))
