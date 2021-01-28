def enkucuk(*par):
    print("Parametreler:",par)
    minimum=par[0]
    if par==():
        return None
    if len(par)==1:
        minumum=par[0]
    
    for i in par:
        if minimum>i:
            minumum=i
        else:
            continue
    return minumum

parametreler=enkucuk(1,2,3,-1,4,-2,5)
print(parametreler)

