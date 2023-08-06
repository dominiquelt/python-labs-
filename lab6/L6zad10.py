n=int(input('podaj n do ktorego mam obliczyc ciag fibbonaciego:'))
a=[]
f=[]
for i in range(n):
    f.append(i)
print(f)
for i in range(n):
    if i==0 or i==1:
        k=1
        a.append(k)
    if i>1:
        z=a[i-1]
        y=a[i-2]
        k=z+y
        a.append(k)
print('ciag fibbonaciego:',a,sep='\n')

