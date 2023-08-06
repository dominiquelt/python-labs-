#Zadanie8
import random
n= random.randint(0, 100)
print("wylosowano: ", n)

suma_kw =(n*(n+ 1)*(2*n+ 1))//6
print("suma kwadratów od 0 do", n,":", suma_kw)