from math import *

class figura:
    def __init__(self,nazwa):
        self.nazwa=nazwa
    def o_czym_mowa(self):
        return "Mamy do czynienia z figura o nazwie {}".format(self.nazwa)

class kwadrat(figura):
    def __init__(self,bok):
        super().__init__("kwadrat")
        self.bok=bok

    def obwod(self):
        o= 4 * self.bok
        print ("Obwod kwadratu wynosi", o)

    def pole(self):
        p = self.bok * self.bok
        print("Pole kwadratu wynosi", p)



class prostokat(figura):
    def __init__(self,bok1,bok2):
        super().__init__("prostokat")
        self.bok1 = bok1
        self.bok2 = bok2

    def obwod(self):
        o= (2 * self.bok1) + (2 * self.bok2)
        print ("Obwod prostokata wynosi", o)

    def pole(self):
        p = self.bok1 * self.bok2
        print("Pole prostokata wynosi", p)




class trojkat(figura):
    def __init__(self,bok1,bok2,bok3,wysokosc1):
        super().__init__("trojkat")
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3=bok3
        self.wysokosc1=wysokosc1

    def obwod(self):
        o = self.bok2 + self.bok1 +self.bok3
        print("Obwod trojkata wynosi", o)

    def pole(self):
        p = (self.bok1*self.wysokosc1) / 2
        print("Pole trojkata wynosi", p)

    def foremny(self):
        if self.bok2==self.bok1==self.bok3:
            print("Jest to trojkat foremny!")


class kolo(figura):
    def __init__(self,promien):
        super().__init__("kolo")
        self.promien=promien

    def obwod(self):
        o = 2 * pi * self.promien
        print("Obwod kola wynosi", o)

    def pole(self):
        p = pi * (self.promien **2)
        print("Pole kola wynosi", p)


class romb(figura):
    def __init__(self,bok,przek1,przek2):
        super().__init__("romb")
        self.bok = bok
        self.przek1=przek1
        self.przek2=przek2

    def obwod(self):
        o= 4 * self.bok
        print ("Obwod rombu wynosi", o)

    def pole(self):
        p = (self.przek1 * self.przek2)/2
        print("Pole rombu wynosi", p)



class trapez(figura):
    def __init__(self,ramie1,ramie2,podst1,podst2,wysokosc):
        super().__init__("trapez")
        self.ramie1=ramie1
        self.ramie2=ramie2
        self.podst1=podst1
        self.podst2=podst2
        self.wysokosc=wysokosc

    def obwod(self):
        o = self.podst2 + self.podst1 +self.ramie2 + self.ramie1
        print("Obwod trapezu wynosi", o)

    def pole(self):
        p = ((self.podst1 + self.podst2)*self.wysokosc) / 2
        print("Pole trapezu wynosi", p)

    def rownoramienny(self):
        if self.ramie2==self.ramie2:
            print("Jest to trapez rownoramienny!")

trapezz=trapez(2,2,12,6,7)
print(trapezz.o_czym_mowa())
print(trapezz.obwod())
print(trapezz.pole())
print(trapezz.rownoramienny())

koloo=kolo(19)
print(koloo.pole())
print(koloo.obwod())


