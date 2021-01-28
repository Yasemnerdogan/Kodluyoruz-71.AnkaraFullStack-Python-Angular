def  fibonacci(n):
    sayi1=0
    sayi2=1
    liste=[0,1]
    for i in range(n-2):
        sayi3=sayi1+sayi2
        liste.append(sayi3)
        sayi1=sayi2
        sayi2=sayi3
    return liste
n=int(input("lütfen kaç adet fibonacci sayı girileceğini belirleyin"))
fibonaccilistesi=fibonacci(n)
print(fibonaccilistesi)
