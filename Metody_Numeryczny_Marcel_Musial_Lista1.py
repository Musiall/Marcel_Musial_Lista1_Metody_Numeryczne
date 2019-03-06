from numpy import *
from matplotlib.pyplot import *

#ZAD1
print('ZAD1. ')
def funkcja_kwadratowa(x):
    return 2*(x**2)+2*x+2
for i in range(56,101):
    print(funkcja_kwadratowa(i))

#ZAD2
print('ZAD2. Silnia')
n=int(input("podaj liczbe: "))

def silnia(n):
    k=1 #zmienna pomocnicza
    i=0 #warunek początkowy
    if n>1:
        while(n!=i):
            i+=1
            k=k*i
        return k
    elif n==1:
        return 1
    elif n==0:
        return 1


print(silnia(n))


#ZAD3
print('ZAD3. Minimum i indeksy')
tab=[14, -2,3, 24,1, 23, 5, 110,-2, 152, 1, 75,1]
indeksy=[]
def min_tab(i):
    minimum=tab[0]
    for i in tab:
        if minimum>i:
            minimum=i
    print(minimum)
    for i in range(len(tab)):
        if tab[i]==minimum:
            indeksy.append(i)

    
    print(indeksy)
min_tab(tab)

#ZAD4

print('ZAD4. Wykres')
a=int(input("Write starting number of the chart"))
b=int(input('Write ending number of the chart'))


x=linspace(a,b,100)
y=sin(x)
xlabel('xLabel')
ylabel('yLabel')
plot(x,y)
show()
