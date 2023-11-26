def extraire_noms_presidents(L):        #avec numero

    liste_noms=[]

    for i in range(len(L)):

        nom = str()
        start = 0

        for caractere in L[i]:

            if caractere == '.':    #si le caractere est un point on arrete enrigistrement du nom
                start = 0

            elif start == 1:        #si start==1 on continue d'apprendre les caracteres du noms
                nom += caractere

            elif caractere == '_':   #si le caractère est un - on peut commencer à apprendre les caracteres du noms
                start = 1

        liste_noms.append(nom)

    return liste_noms




