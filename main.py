def extraire_noms_presidents(L):

    liste=[]

    for i in range(len(L)):         #obtenir nom avec numero

        nom = str()
        start = 0

        for caractere in L[i]:

            if caractere == '.':    #si le caractere est un point on arrete enrigistrement du nom
                start = 0

            elif start == 1:        #si start==1 on continue d'apprendre les caracteres du noms
                nom += caractere

            elif caractere == '_':   #si le caractère est un - on peut commencer à apprendre les caracteres du noms
                start = 1

        liste.append(nom)

        liste_noms=[]
        for i in range(len(liste)): #enlever numero

            nom = str()

            for car in liste[i]:

                if not 48<=ord(car)<=59:
                    nom+=car

            liste_noms.append(nom)

        liste_nom_final=[]
        liste_nom_final.append((liste_noms[0]))

        for i in range(1, len(liste_noms)):

            if not liste_noms[i] in liste_nom_final:
                liste_nom_final.append(liste_noms[i])

    return liste_nom_final



