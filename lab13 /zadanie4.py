class student:
    def __init__(self,imie,nazwisko, wiek, rokstudiow, kierunek, hobby, samopoczucie, zwierze):
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.rokstudiow=rokstudiow
        self.kierunek=kierunek
        self.hobby=hobby
        self.samopoczucie=samopoczucie
        self.zwierze=zwierze
    def legitymacja(self):
        return "Nazywam się {} {}, studiuje {}, na {} roku".format(self.imie,self.nazwisko,self.kierunek,self.rokstudiow)
    def kierunek(self):
        print("Co studiujesz?")
        if self.kierunek == "informatyka":
            print("Good luck with that...")
        else:
            print("Wow!")
    def jaktam(self):
        if self.samopoczucie< 50:
            if self.zwierze != "brak":
                return "Pogłaszcz {}".format(self.zwierze)
            else:
                if wiek >=18:
                    print("Jakie mamy alternatywy?")
                else:
                    print (":((")
    def czaswolny(self):
        return "W wolnym czasie lubie {}".format(self.hobby)
stu=student("Jan", "Kowalski",20,2,"informatyka", "gotowanie", 49, "kot")
print(stu.legitymacja())
print(stu.czaswolny())
print(stu.jaktam())
print(stu.kierunek())

