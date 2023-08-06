class pojazd:
    def __init__(self,tablica):
        self.tablica=tablica
    def __del__(self):
        print("Pojazd usuwany z pamieci")
    def start(self):
        print("odpalam")
    def stop(self):
        print('STOP')
    def tablicowanie(self):
        return "{} oto nr tablicy rejestracyjnej pojazdu".format(self.tablica)

class auto(pojazd):
    def __init__(self,tablica):
        super().__init__(tablica)
        self.ilosckol=4
    def jazda(self):
        return "Poruszam sie na {} kolach!".format(self.ilosckol)

class motocykl(pojazd):
    def __init__(self,tablica):
        super().__init__(tablica)
        self.ilosckol=2
    def jazdamot(self):
        return "Poruszam sie na {} kolach!".format(self.ilosckol)

moto=motocykl(78844)

print(moto.tablicowanie())
print(moto.stop())
print(moto.jazdamot())




