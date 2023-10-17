def complement_2():
    while len(liste) < 8:
        liste.insert(0, "0")
    indice1 = 0
    for i in range(len(liste)-1,-1,-1):
        if liste[i] == "1":
            indice1 = i
            break
    liste1 = liste[:indice1]
    liste2 = liste[indice1:]
    liste3=[]
    for i in range(0, len(liste1)):
        if liste1[i] == "0" :
            liste3.append("1")
        else:
            liste3.append("0") 

    liste_final = liste3+liste2
    return liste_final    


nb_binaire = input("Entre un nombre binaire (nombre caractere < 8) : ")
liste = []

for i in range (0,len(nb_binaire)):
    liste.append(nb_binaire[i])
    
a = complement_2()
complement2 = "".join(a)
print("Le nombre devient donc", complement2)