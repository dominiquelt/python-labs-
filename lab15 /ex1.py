class restaurant:
    def __init__(self,rodzaj,nazwa):
        self.rodzaj=rodzaj
        self.nazwa=nazwa
    def coto(self):
        return "To restauracja {}, nazywa się {}".format(self.rodzaj,self.nazwa)


class IceCreamStand(restaurant):
    def __init__(self,nazwa):
        super().__init__("lodziarnia",nazwa)
        self.smaki=['wanilia','czekolada','pistacja','herbatniki','truskawka']
        self.podanie=['wafelek', 'kubeczek']

    def jakiesmaki(self):
        for element in self.smaki:
            print( "----->", element)

    def podanie(self):
        print("Sposoby podania:")
        for element in self.podanie:
            print("------>", element)

class CoffeeShop(restaurant):
    def __init__(self,nazwa):
        super().__init__("kawiarnia",nazwa)
        self.kawy=["latte","americano",'espresso','espresso doppio','flat white']
        self.podanie=['na miejscu', 'na wynos']

    def jakiekawy(self):
        for element in self.kawy:
            print( "----->", element)

    def podaniepytanie(self):
        print("Sposoby podania:")
        for element in self.podanie:
            print("------>", element)
        x=int(input("Jak podać? Po wpisaniu 1 - kawa na miejscu, po wpisaniu 2 -kawa na wynos:"))
        if x==1:
            print("Oto kawa na miejscu.")
        elif x==2:
            print("Oto kawa na wynos.")
        else:
            print("Brak decyzji")

kawa=CoffeeShop("Coffee")
lody=IceCreamStand("IceCream")
print(lody.jakiesmaki())
print(kawa.coto())
print(kawa.podaniepytanie())

