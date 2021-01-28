devam=1
while devam==True:
    oyuncu1=input("oyuncu1,taş mı? kağıt mı ? makas mı ?")
    oyuncu2=input("oyuncu2 taş mı? kağıt mı ? makas mı ?")
    if oyuncu1=="makas":
        if oyuncu2=="makas":
            print("Berabere kaldınız")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        elif oyuncu2=="taş":
            print("taş makası ezer.Tebrikler oyuncu2 kazandı")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        else:
            print("makas kağıdı keser. Tebrikler oyuncu1 kazandı.")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
    elif oyuncu1=="kağıt":
        if oyuncu2=="kağıt":
            print("berabere kaldınız")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        elif oyuncu2=="makas":
            print("makas kağıdı keser. Tebrikler oyuncu2 kazandı.")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        else:
            print("kağıt taşı sarar.Tebrikler oyuncu2 kazandı")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
            
    elif oyuncu1=="taş":
        if oyuncu2=="taş":
            print("berabere kaldınız")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        elif oyuncu2=="makas":
            print("taş makası ezer.Tebrikler oyuncu1 kazandı")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
        else:
            print("kağıt taşı sarar.Tebrikler oyuncu2 kazandı")
            devam=int(input("devam etmek için 1'e yeni bir oyun için 0'a basın"))
    
    else:
        print("lütfen geçerli bir giriş yapın ")
        continue
