from random import randint

def letterNumberSwap(x):
    # change letters to numbers and vice versa
    if x == "A":
        return 1
    elif x == "B":
        return 2
    elif x == "C":
        return 3
    elif x == "D":
        return 4
    elif x == "E":
        return 5
    elif x == "F":
        return 6
    elif x == "G":
        return 7
    elif x == "H":
        return 8
    elif x == 1:
        return "A"
    elif x == 2:
        return "B"
    elif x == 3:
        return "C"
    elif x == 4:
        return "D"
    elif x == 5:
        return "E"
    elif x == 6:
        return "F"
    elif x == 7:
        return "G"
    elif x == 8:
        return "H"
    else:
        print("Something is wrong.")

moveList = [] # list of moves in matrix connotation
possibleMoves = [] # list of moves in chess connotation

def athareket(position):
    # calculate all knight moves from position
    column, row = list(position.strip().upper())
    column = letterNumberSwap(column)
    c,r = (int(column), int(row))
    if (0 < (c - 2) <= 8):
        if (0 < (r - 1) <= 8):
            moveList.append((c - 2, r - 1))
        if (0 < (r + 1) <= 8):
            moveList.append((c - 2, r + 1))
    if (0 < (c - 1) <= 8):
        if (0 < (r - 2) <= 8):
            moveList.append((c - 1, r - 2))
        if (0 < (r + 2) <= 8):
            moveList.append((c - 1, r + 2))
    if (0 < (c + 1) <= 8):
        if (0 < (r - 2) <= 8):
            moveList.append((c + 1, r - 2))
        if (0 < (r + 2) <= 8):
            moveList.append((c + 1, r + 2))
    if (0 < (c + 2) <= 8):
        if (0 < (r - 1) <= 8):
            moveList.append((c + 2, r - 1))
        if (0 < (r + 1) <= 8):
            moveList.append((c + 2, r + 1))
            
    for entry in moveList:
        # back to chess connotation
        possibleMoves.append(letterNumberSwap(entry[0])+str(entry[1]))

başlangıckonum=input("atın konumunu girin bir kenarını A,B,C,D,E,F,G,H diğer kenarını 1,2,3,4,5,6,7,8 den seçin A1 B2 gibi")
athareket(başlangıckonum)
print("At " + başlangıckonum + "için gidebileceği konumlar:")
liste=[]
for entry in possibleMoves:
    a=tuple(entry)
    liste.append(a)
print(liste)
    
