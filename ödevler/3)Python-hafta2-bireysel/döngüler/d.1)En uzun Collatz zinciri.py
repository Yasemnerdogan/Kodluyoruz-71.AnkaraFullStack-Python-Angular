
has2={}
def collatz(x):
    liste=[]
    liste.append(x)
    sayi=x
    while(sayi>1):
        if sayi%2==0:
            sayi=int(sayi/2)
            if sayi in has2:
                liste+=has2[sayi]
                break
            else:
                liste.append(sayi)
        else:
            sayi=3*sayi+1
            if sayi in has2:
                liste+=has2[sayi]
                break
            else:
                liste.append(sayi)


    has2[x]=liste           
    return len(liste)

num=0
greatest=0
for i in range(1000000):
    c=collatz(i)
    if num<c:
        num=c
        greatest=i
print('{0} has {1} elements.'.format(greatest,num))
