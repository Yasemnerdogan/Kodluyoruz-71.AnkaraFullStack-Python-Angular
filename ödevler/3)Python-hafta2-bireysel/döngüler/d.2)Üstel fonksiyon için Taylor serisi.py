
import math
def üstel(x, hata = 10**(-10)):
    n = 1
    sonterim = 1 # serideki ilk terimimiz
    toplam = sonterim
    while sonterim >= hata:
        
        sonterim = sonterim * x/n # yeni terim bir öncekini x ile çarpıp terim sıra numarasına bölerek bulunuyor.
        toplam += sonterim
        n += 1
    return n,toplam,sonterim
    
x=int(input("x degerini girin "))
n,toplam,sonterim=üstel(x)
print("e^x:",toplam)
print(n,"terim kullanıldı")
print("son terim:",sonterim)

