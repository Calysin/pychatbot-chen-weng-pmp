#Import des bibliothèques
import os
import math
def list_of_files(directory, extension): #Code donné pour le projet permettant d'obtenir les fichiers
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def extraire_noms_presidents(L): #Fonction permettant d'extraire les noms des présidents sans nombre
    liste=[] #Liste stockant les noms des présidents extrait
    for i in range(len(L)): #Boucle obtenant les noms avec les numeros
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
        for i in range(len(liste)): #Boucle enlevant les numéros
            nom = str()
            for car in liste[i]:
                if not 48 <= ord(car) <= 59: #Si l'ascii du caractere n'est pas un chiffre
                    nom += car    #Stock les caracteres du nom
            liste_noms.append(nom)
        liste_nom_final=[]
        liste_nom_final.append((liste_noms[0])) #Liste finale stock le 1er nom
        for i in range(1, len(liste_noms)):
            if not liste_noms[i] in liste_nom_final: #si le nom n'est pas dans
                liste_nom_final.append(liste_noms[i])
    return liste_nom_final


def association_prenom(L): #Fonction associant les prénoms aux noms
    liste_complete=[]
    for i in range(len(L)): #Pour chaque nom dans la liste obtenue dans la dernière fonction, ajouté son prénom
        if L[i] == 'Chirac':
            liste_complete.append('Jacques '+L[i])
        elif L[i] == 'Giscard dEstaing':
            liste_complete.append('Valéry ' + L[i])
        elif L[i] == 'Hollande' or L[i] == 'Mitterrand':
            liste_complete.append('François ' + L[i])
        elif L[i] == 'Macron':
            liste_complete.append('Emmanuel ' + L[i])
        elif L[i] == 'Sarkozy':
            liste_complete.append('Nicolas ' + L[i])
    return liste_complete

def print_noms(L):  #Fonction affichant les nom et prénoms des présidents obtenu dans la précédente fonction
    for i in range(len(L)):
        print(L[i])

def extraire_noms_avec_numero(L): #Fonction qui extrait les noms des présidents avec les numéros cette fois-ci
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

def ConversionMajusculeEnMinuscule(L): #Fonction convertissant les majuscules présentes dans les fichiers en minuscules
    ListeNomNum = extraire_noms_avec_numero(L)  #Créer une variable appelant la fonction extraire_noms_avec_numero
    for i in range(len(ListeNomNum)):
        with open("speeches/Nomination_{}.txt".format(ListeNomNum[i]), "r") as f, open("cleaned/CleanedNomination_{}.txt".format(ListeNomNum[i]), "w") as f1: #Ouvre deux fichiers, le premier en f en mode lecture et le deuxième en f1 en mode écriture
            contenu = f.readlines() #Retranscrit les minuscules et change les majuscules en minuscule
            for ligne in contenu:
                for lettre in ligne:
                    if 65 <= ord(lettre) <= 90:
                        LettreMinuscule = lettre.lower()
                        f1.write(LettreMinuscule)
                    else:
                        f1.write(lettre)

def del_ponctuations(L): #Fonction supprimant la ponctuation
    ponctuation = ['!', ':', ";", '?', '.', ',', '(', ')', '{', '}', '[', ']'] #Liste de caractère devant être supprimé ou remplacé par un espace
    special=["'", '"', '-']
    liste_nom_numero= extraire_noms_avec_numero(L) #Créer une variable appelant la fonction extraire_noms_avec_numero
    for i in range(len(liste_nom_numero)): #Boucle permettant de parcourir tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r', encoding="utf-8")as f:
            contenu=f.readlines()
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'w', encoding="utf-8")as f:
            for ligne in contenu: #Supprime tous les caractères devant l'être ou les remplaces par un espace
                for car in ligne:
                    if car in special:
                        f.write(" ")
                    elif not car in ponctuation:
                        f.write(car)
def TF(ch):
    list_mot=ch.split()     #sépare la chaine de caractere dans une liste
    dictionnaire= {}
    for i in range(len(list_mot)):  #boucle permettant de parcourir la liste mot
        repet=0
        for mot in list_mot:        #parcourir mot de la liste
            if list_mot[i]==mot:    #si la valeur de la liste est mot
                repet+=1            #incremente repet
        dictionnaire[list_mot[i]]=repet #dictionnaire de la valeur de la liste vaut repet

    return dictionnaire

def IDF(L): #Fonction calculant l'IDF
    NbTotalDoc = 0 #Initie les variables
    mots_par_document = {}
    mots_globaux = set()
    for nom_numero in L: #Compte le nombre de documents et mots
        with open(f"cleaned/Cleaned{nom_numero}", "r", encoding="utf-8") as f:
            contenu = f.read().split()
            NbTotalDoc += 1
            mots_par_document[nom_numero] = set(contenu)
            mots_globaux.update(contenu)
    scores_IDF = {}  #Calcul le scoreIDF pour chaque mot
    for mot in mots_globaux:
        NbDocAvecMot = sum(mot in mots_par_document[nom_numero] for nom_numero in L) + 1
        score_IDF = math.log(((NbTotalDoc / NbDocAvecMot)+1))
        scores_IDF[mot] = score_IDF
    return scores_IDF

def transpose_matrice(M):
    matrice_final=[]

    for j in range(len(M[0])):          #boucle range la plus grande longueur de ligne
        L=[]
        for i in range(len(M)):     #boucle range longueur de la matrice
            L.append(M[i][j])   #on apprend

        matrice_final.append(L)

    return matrice_final


def TF_IDF(files_names):

    liste_nom_numero = extraire_noms_avec_numero(files_names)  #liste de tout les noms avec numero
    matrice_tf_idf = []
    mot_tf = []

    for i in range(len(liste_nom_numero)):  # Boucle permettant de parcourir tous les fichiers, et de calculer chaque tf-idf d'un mot dans un fichier

        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r', encoding="utf-8") as f:
            contenu = f.read()

        tf = TF(contenu)

        for mot in tf:              #en dehors de la 2eme i boucle pour éviter que la premiere colonne ne correspond pas au fichier
            if mot not in mot_tf:
                mot_tf.append(mot)  #liste contenant tt les mots sans doublon et gardant le meme ordre


    for i in range(len(liste_nom_numero)):  # Boucle permettant de parcourir tous les fichiers, et de calculer chaque tf-idf d'un mot dans un fichier
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r', encoding="utf-8") as f:
            contenu=f.read()

        tf = TF(contenu)        #tf de ce fichier
        idf = IDF(files_names)  #idf de tt les fichiers

        L=[]

        for mot in mot_tf:

            if mot in tf:
                L.append((tf[mot] * idf[mot]))  #apprend le tf-idf de chaque mot de ce fichier
            else:
                L.append(0)                     #si le mot n'existe pas dans ce fichier = 0

        matrice_tf_idf.append(L)            #matrice, ligne: fichier, colonne: tf-idf de chaque mot du fichier

    tf_idf=transpose_matrice(matrice_tf_idf)    #transpose matrice pour avoir les lignes et les colonnes inversé

    return tf_idf, mot_tf

def tf_idf_max(files_names):

    tf_idf, liste_mot = TF_IDF(files_names)     #prend la matrice if-idf et la liste des mots, chaque ligne des 2 corresponds au même mot

    tfidf_max = 0
    for i in range(8):
        tfidf_max += tf_idf[0][i]              #initialise une valeur a tt ces variables pour pouvoir trouver le max
    mot = liste_mot[0]


    for i in range(len(tf_idf)):
        somme_tfidf=0

        for j in range(len(tf_idf[i])):
            somme_tfidf += tf_idf[i][j]

        if tfidf_max<somme_tfidf:

            print(tfidf_max, somme_tfidf, mot)

            tfidf_max=somme_tfidf
            mot = liste_mot[i]


    detail_max=[tfidf_max, mot]   # liste avec l[0]=le plus grand tf-idf, l[1]=le mot correspondant et l[2]=le fichier correspondant

    return detail_max

def tf_idf_0(files_names):
    tf_idf, liste_mot = TF_IDF(files_names)  # prend la matrice if-idf et la liste des mots, chaque ligne des 2 corresponds au même mot

    L_mot_non_important=[]
    for i in range(len(tf_idf)):
        fichier_8=0
        for j in range(len(tf_idf[i])):

            if round(tf_idf[i][j])==0:
                fichier_8 += 1

        if fichier_8==8:
            L_mot_non_important.append(liste_mot[i])

    return L_mot_non_important

