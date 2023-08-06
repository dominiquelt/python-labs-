class samochod:
    def __init__(self, marka, model, przebieg, wartosc, kolor):
        self.marka=marka
        self.model=model
        self.przebieg=przebieg
        self.wartosc=wartosc
        self.kolor=kolor
    def jedzprosto(self,przejazd):
        self.przebieg += przejazd
    def zatrab(self):
        print("HOOOOOONK!")
    def czasnamycie(self,kolorteraz):
        if kolorteraz != self.kolor:
            print("Czas na mycie!")
        else:
            print("czysty!")
    def prawo(self):
        print("Skręcam w prawo.")
    def lewo(self):
        print("Skręcam w lewo")

ferrari= samochod("Ferrari","Spider",0,990000,"czerwony")
opel= samochod("Opel","Corsa",30000,15000,"biały")
ram= samochod("RAM", "1500 TRX",0, 291000, "czarny")
toyota = samochod("Toyota", "Corolla", 7000, 940000,"srebrny")
audi = samochod("Audi", "A4",0,178000, "biały")


print(ferrari.czasnamycie())
