import random
A=[]
for i in range(101):
    A.append(i)
print(A)
B=[]
for i in range(10):
    x=random.choice(A)
    B.append(x)
print('wygenerowana lista:',B)
random.shuffle(B)
print('lista pomieszana:',B)
B.sort()
print('lista posortowana:',B)

