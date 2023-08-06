#1 stopa to 0,3048 metra.
x=float(input("Podaj długość w stopach:"))
def stopyfunkcja(a):
    metry= a*0.3048
    kilometry= a*0.3048/1000
    centymetry= a*0.3048*100
    milimetry= a*0.3048*1000
    print(x,"ft to:","\n", metry,"metrów", "\n", kilometry, "kilometrtrów", "\n", centymetry, "centrymetrów", "\n", milimetry, "milimetrów")

print(stopyfunkcja(x))
