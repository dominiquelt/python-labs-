stopy= int(input(" wysokość w stopach:"))
cale= int(input(" wysokość w cm:"))

sumacali = stopy*1+ cale
m= sumacali*0.0254
cm= m*100
mm= cm*10
km= mm/1000

print("Wysokość w metrach: ", m)
print("Wysokość w cm: ", cm)
print("Wysokość w mm: ", mm)
print("Wysokość w km: ", km)
