def Mukemmel(sayi):
    toplam=0;
    for i in range(1,sayi):
        if sayi%i==0:
            toplam+=i
    if toplam==sayi:
        return True
    else:
        return False
 
for sayi in range(0,10000):
    
    mükemmelmi=Mukemmel(sayi)
    if mükemmelmi== True:
        print(sayi)
    
