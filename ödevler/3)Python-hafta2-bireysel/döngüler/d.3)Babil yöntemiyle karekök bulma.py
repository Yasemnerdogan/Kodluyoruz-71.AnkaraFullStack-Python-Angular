n=1
N=float(input("karekökü alınacak sayı:"))
xönceki=int(input("ilk tahmin"))

tol=10**(-10)
hata=abs((xönceki**2)-N)
while hata>tol:
        xsonraki=(xönceki+(N/xönceki))/2
        xönceki=xsonraki
        hata=abs((xönceki**2)-N)
        n=n+1
print("karekök:",xönceki)
print(n,"iterasyon")
        
    

