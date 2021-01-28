def karekök(N,xönceki,tol=10**(-10),maxiter=15):
    n=1
    hata=abs((xönceki**2)-N)
    while hata>tol:
        if n>maxiter:
            print("10 iterasyonda sonuca ulaşılamadı. 'hata' veya 'maxiter' değerlerini değiştirin")
            break
        
        xsonraki=(xönceki+(N/xönceki))/2
        xönceki=xsonraki
        hata=abs((xönceki**2)-N)
        n=n+1
        
    return xönceki

a=karekök(N=10,xönceki=1)
print(a)

        
    
