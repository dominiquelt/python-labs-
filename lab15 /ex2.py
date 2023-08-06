class beer:
    def __init__(self,nazwa,cena,procent,ocena,pochodzenie):
        self.nazwa=nazwa
        self.cena=cena
        self.procent=procent
        self.ocena=ocena
        self.pochodzenie=pochodzenie
lista_piw=[]
class piwojasneciemne(beer):
    def __init__(self,nazwa,cena,procent,ocena,pochodzenie,rodzaj):
        super().__init__(nazwa,cena,procent,ocena,pochodzenie)
        self.rodzaj=rodzaj

    def jakie(self):
        piwo_jasne=[]
        piwo_ciemne=[]
        for x in lista_piw:
            if x.rodzaj=="ciemne":
                piwo_ciemne.append(x)
            else:
                piwo_jasne.append(x)
class sklep:
    def __init__(self,nazwa):
        self.nazwa=nazwa
        self.asortyment=[]
    def dodaj_asortyment(self,beer):
        self.asortyment.append(beer)

    def odnajwyzszej(self):
        posortowane=sorted(self.asortyment, key=lambda x: x.cena, reverse=True)
        return posortowane

piwo1=piwojasneciemne("Tyskie",4.0,5.2,3.5,"Polska",'jasne')
piwo2=piwojasneciemne("Staropramen",7.5,5.0,4.0,"Czechy",'jasne')
piwo3=piwojasneciemne("Fortuna",8.0,5.6,3.78,'Polska','ciemne')

lista_piw=[piwo1,piwo2,piwo3]

sklep1=sklep("ABC")
sklep1.dodaj_asortyment(piwo1)
sklep1.dodaj_asortyment(piwo2)
sklep1.dodaj_asortyment(piwo3)

piwo1.jakie()

posortowane_cena = sklep1.odnajwyzszej()

print("Posortowane piwa:")
for x in posortowane_cena:
    print(f"{x.nazwa}:{x.cena}")





