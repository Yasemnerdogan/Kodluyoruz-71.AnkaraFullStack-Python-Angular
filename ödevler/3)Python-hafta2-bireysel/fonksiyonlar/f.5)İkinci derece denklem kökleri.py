import cmath
def kök(a,b,c):
    #y=ax^2+bx+c
    diskriminant=b**2-4*a*c
   
    if a==0:
        kök=(-c/b)
        return kök
    else:
        karekök=cmath.sqrt(diskriminant)
        x1=(-b-karekök/(2*a))
        x2=(-b+karekök/(2*a))
        kök=(x1,x2)
        return kök
        
a=int(input("a degerini girin: "))
b=int(input("b degerini girin: "))
c=int(input("c degerini girin: "))
kökler=kök(a,b,c)
print(kökler)
    
 

 
