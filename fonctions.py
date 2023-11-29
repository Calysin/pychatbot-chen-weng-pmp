import os
def list_of_files(directory, extension):

    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


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

                if not 48<=ord(car)<=59: #si l'ascii du caractere n'est pas un chiffre
                    nom+=car    #stocke les caracteres du nom

            liste_noms.append(nom)

        liste_nom_final=[]
        liste_nom_final.append((liste_noms[0])) #la liste finale stock le 1er nom

        for i in range(1, len(liste_noms)):

            if not liste_noms[i] in liste_nom_final:    #si le nom n'est pas dans
                liste_nom_final.append(liste_noms[i])

    return liste_nom_final


def association_prenom(L):

    liste_complete=[]

    for i in range(len(L)): #si nom = differente proposition, associer le prenom donnée

        if L[i]== 'Chirac':
            liste_complete.append('Jacques '+L[i])

        elif L[i]== 'Giscard dEstaing':
            liste_complete.append('Valéry ' + L[i])

        elif L[i] == 'Hollande' or L[i] == 'Mitterand':
            liste_complete.append('François ' + L[i])

        elif L[i] == 'Macron':
            liste_complete.append('Emmanuel ' + L[i])

        elif L[i] == 'Sarkozy':
            liste_complete.append('Nicolas ' + L[i])

    return liste_complete

def print_noms(L):  #print noms
    for i in range(len(L)):
        print(L[i])


def extraire_noms_avec_numero(L):
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
    return liste

def del_ponctuations(L):
    ponctuation = ['!', ':', ";", '?', '.', ',', '(', ')', '{', '}', '[', ']'] #caractere devant être delete
    special=["'", '"', '-'] #caractere devant etre remplacer par un espace
    liste_nom_numero= extraire_noms_avec_numero(L)  #noms avec numero

    for i in range(len(liste_nom_numero)):  #boucle permettant de parcourir tt les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r')as f:
            contenu=f.readlines()
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'w')as f:
            for ligne in contenu:
                for car in ligne:
                    if car in special:  #si car est un caractere de ponctuation special, write espace
                        f.write(" ")
                    elif not car in ponctuation: #si car est un caractere de ponctuation, write le caractere
                        f.write(car)

