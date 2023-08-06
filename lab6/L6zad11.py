import math
x=int(input("Jak długi ciąg zamierzasz rozpatrywać?:"))
pierwiastek= int(math.sqrt(x))
print(pierwiastek)

A=[]
for i in range(2,x+1):
    A.append(i)

n=0
while A[n]<=pierwiastek:
    for i in A:
        if i%A[n]==0 and i!=A[n]:
            A.remove(i)
    print(A)
    n+=1

