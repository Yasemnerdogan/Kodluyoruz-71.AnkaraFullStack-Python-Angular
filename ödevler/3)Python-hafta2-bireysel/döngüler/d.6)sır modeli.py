s_eski = 99/100
i_eski = 1/100
r_eski = 0/100
a=0.6
b=0.2
s = s_eski - a * i_eski * s_eski
i = i_eski + a* i_eski * s_eski - b * i_eski
r = r_eski + b * i_eski
toplam=s+i+r
enazhastasayısı=100
adet=0
print("t","   s   ","  i  ","  r  "," toplam")
while i>0.1/100 and adet<=100:
    s = s_eski - a * i_eski * s_eski
    
    i = i_eski + a* i_eski * s_eski - b * i_eski
    
    r = r_eski + b * i_eski
    
    toplam=s+i+r
    print("   t: ",adet,"   s: ",s,"    i: ",i,"  r: ",r ,"     toplam ",round(toplam,1))
    s_eski=s
    i_eski=i
    r_eski=r
    if enazhastasayısı>i:
        enazhastasayısı=i
        azamihasta=(adet,".zaman adımında azami hasta sayısına  ulaşır ve hastasayısı:",enazhastasayısı)
    adet=adet+1
print(azamihasta)



    
    

