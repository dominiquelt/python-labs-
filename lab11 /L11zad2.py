celsjusz= int(input('podaj stopnie w celsjuszach:'))
cel_Fah = celsjusz * 9 / 5 + 32
print('celjsusze na Fahrenheit: ', cel_Fah)

fahrenheit = int(input("podaj stopnie w fahrenheitach:"))
fah_Cel = (Fahrenheit - 32) * 5 / 9
print('Ffahrenheit na celsjusze: ', fah_cel)

kelvin = int(input("podaj stopnie w kelvinach: "))
cel_kel = celsjusz + 273.15
print("celsjusze na kelviny: ", cel_kel)

kel_cel = kelvin - 273.15
kel_fah = (kelvin - 273.15) * 9/5 + 32
fah_kel = (fahrenheit - 32) * 5/9 + 273.15
print("kelviny na celsjusze: ", kel_cel)
print("kelviny na fahrenheit: ", kel_fah)
print("fahrenheit na kelviny: ", fah_kel)

temp_cel = int(input("podaj temperaturę w celsjuszach: "))
temp_fah = temp_cel * 9 / 5 + 32

if temp_fah < 32:
    print(f"woda zamarza przy: {temp_fah:.2f}°F")
elif temp_Fah > 212:
    print(f"woda zaczyna wrzec od: {temp_fah:.2f}°F")
else:
    print(f"temperatura w stopniach fahrenheita wynosi: {temp_fah:.2f}°F")
