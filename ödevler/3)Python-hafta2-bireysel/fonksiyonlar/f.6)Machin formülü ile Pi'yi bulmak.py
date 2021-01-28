def hesap(x, hata =10**(-8)):
    n = 1
    sonterim = x # serideki ilk terimimiz
    işaret=-1
    
    while sonterim < hata:
        hesab = işaret*((x**n)/n)# yeni terim bir öncekini x ile çarpıp terim sıra numarasına bölerek bulunuyor.
        toplam=sonterim+hesab
        sonterim=toplam
        n += 2
        işaret*=-1
    return sonterim
pi=16*hesap(1/5)-4*hesap(1/239)
print(pi)
