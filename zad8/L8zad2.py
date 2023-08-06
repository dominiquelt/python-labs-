kontakty={'ala':123456789,'kasia':786954567,'patrycja':100090909,'kot':78265675,'pies':112343232,'ola':232425262,'olek':198765432,'olaf':666666666,'kacper':999988888,'kot2':987678987}
print(kontakty)
kontakty['basia']= kontakty['ala']
del kontakty['ala']
kontakty['burek']= kontakty['kot2']
del kontakty['kot2']
print(kontakty)

for klucz in list(kontakty.keys()):    #słownik da sie skonwertować na listę
    if klucz != 'kasia' and klucz!= 'burek':
        del kontakty[klucz]
print(kontakty)
kontakty.clear()

kontakty['Alan']=505505505
kontakty['Zosia']=123456789
x= list(kontakty)
sorted(x)
print(kontakty)
