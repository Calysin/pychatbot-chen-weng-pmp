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
        NbDocAvecMot = sum(mot in mots_par_document[nom_numero] for nom_numero in L)
        score_IDF = math.log10(NbTotalDoc / NbDocAvecMot)
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
                L.append(round(tf[mot] * idf[mot], 2))  #apprend le tf-idf de chaque mot de ce fichier
            else:
                L.append(0)                     #si le mot n'existe pas dans ce fichier = 0
        matrice_tf_idf.append(L)            #matrice, ligne: fichier, colonne: tf-idf de chaque mot du fichier
    tf_idf=transpose_matrice(matrice_tf_idf)    #transpose matrice pour avoir les lignes et les colonnes inversé
    return tf_idf, mot_tf


def tf_idf_0(files_names):
    tf_idf, liste_mot = TF_IDF(files_names) # prend la matrice if-idf et la liste des mots, chaque ligne des 2 corresponds au même mot
    L_mot_non_important=[]                  #creer liste qui va stocker les mots les moins important

    for i in range(len(tf_idf)):
        fichier_8=0
        for j in range(len(tf_idf[i])):

            if tf_idf[i][j]==0:
                fichier_8 += 1              #si le tf-idf du mot dans un fichier est egal à 0 on incremente la variables fichier8
        if fichier_8==8:                    #si fichier8 == 8 est donc que tt les tf-idf d'un mot dans chaque fichier vaut 0
            L_mot_non_important.append(liste_mot[i])    #la liste apprend le mot correspondant

    return L_mot_non_important

def tf_idf_max(files_names):            #retourne dictionnaire des mots avec les plus grans tf-idf
    tf_idf, liste_mot = TF_IDF(files_names)     #prend la matrice if-idf et la liste des mots, chaque ligne des 2 corresponds au même mot

    tmp_val = 0
    tfidf_max=[]
    mot=[]


    for i in range(len(tf_idf)):

        for j in range(len(tf_idf[i])):
            if tmp_val<tf_idf[i][j]:                       #si cette somme est plus grande que tfidf_max
                tfidf_max=[]
                tfidf_max.append(tf_idf[i][j])               #tfidf_max devient cette somme
                tmp_val=tf_idf[i][j]

                mot=[]
                mot.append(liste_mot[i])                         #on stock le mot correspondant

            elif tmp_val==tf_idf[i][j]: #apprendre une autre variable dans la liste si elle a autant de repetition que le(s) mot(s) deja stocker
                tfidf_max.append(tf_idf[i][j])  # tfidf_max devient cette somme
                mot.append(liste_mot[i])

    return mot


def mot_plus_repet(nom, files_names):
    list_nom=[]
    if nom=='Chirac' or nom=='Mitterrand':  #si c chirac ou mitterrand on prend en compte le fait qu'ils ont 2 discours
        nom1 = nom+'1'
        nom2 = nom+'2'
        list_nom.append(nom1)
        list_nom.append(nom2)
    else:
        list_nom.append(nom)

    dictionnaire={}
    for i in range(len(list_nom)):  # Boucle permettant de parcourir les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(list_nom[i]), 'r', encoding="utf-8") as f:
            contenu=f.read()
        tf = TF(contenu)            #obtient dictionnaire du fichier
        for mot in tf:
            if mot in dictionnaire:
                dictionnaire[mot] += tf[mot]    #si le mot est dans dictionnaire, on ajouter juste la valeur d'occurence du mot à celle existante
            else:
                dictionnaire[mot] = tf[mot]     #sinon dictionnaire apprend ce mot et sa valeur

    liste_mot=[mot]             #prend un mot et sa valeur au pif pour pouvoir comparer
    mot_plus=dictionnaire[mot]
    mot_non_imp=tf_idf_0(files_names)

    for mot in dictionnaire:
        if dictionnaire[mot] > mot_plus and mot not in mot_non_imp:    #si le mot à une plus grande valeur que celle stoker
            liste_mot=[]                    #on supprime ceux stocker
            liste_mot.append(mot)           #et on apprend le nouveau mot et sa valeur
            mot_plus = dictionnaire[mot]
        elif dictionnaire[mot] == mot_plus and mot not in mot_non_imp: #apprendre une autre variable dans la liste si elle a autant de repetition que le(s) mot(s) deja stocker
            liste_mot.append(mot)
    print(liste_mot)

def Nation(L): #Fonction permettant de calculer
    DicoPresidentNation = {} #Déclaration des valeurs
    ListeNomNum = extraire_noms_avec_numero(L)
    ListeNom = []
    for k in range(len(ListeNomNum)): #Boucle créant la definition contenant tous discours des présidents en clé et avec 0 en valeurs pour tous
        DicoPresidentNation[ListeNomNum[k]] = 0
    for i in range(len(ListeNomNum)):  #Boucle parcourant tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(ListeNomNum[i]), 'r') as f:
            contenu = f.read()
            compteurNation = contenu.count("nation")
            DicoPresidentNation[ListeNomNum[i]] = compteurNation #Donne le nombre de fois qu'un président a dit nation en valeur de la définition
    DicoPresidentNation["Chirac"] = DicoPresidentNation["Chirac1"] + DicoPresidentNation["Chirac2"] #Additionne les deux discours de Chirac dans la definition
    DicoPresidentNation.pop("Chirac1")
    DicoPresidentNation.pop("Chirac2")
    DicoPresidentNation["Mitterand"] = DicoPresidentNation["Mitterrand1"] + DicoPresidentNation["Mitterrand2"] #Pareil pour Mitterrand
    DicoPresidentNation.pop("Mitterrand1")
    DicoPresidentNation.pop("Mitterrand2")
    for item in DicoPresidentNation: #Mettre les items/clés de la définition dans une liste
        ListeNom.append(item)
    for j in range(len(ListeNom)): #Boucle pour supprimer les items/clés ou la valeur est 0
        if DicoPresidentNation[ListeNom[j]] == 0:
            DicoPresidentNation.pop(ListeNom[j])
    return sorted(DicoPresidentNation.items(), key = lambda x:x[1], reverse=True) #Change l'affichage de la définition

def ResultatNation(L): #Fonction pour afficher la définition sans le nombre de fois que les presidents disent nation et proprement dans une liste
    ListePresidentNation = []
    for i, j in Nation(L):
        ListePresidentNation.append(i)
    return ListePresidentNation

def PremierClimat(L):
    ListeNomNum = extraire_noms_avec_numero(L)
    MinimalLigne = 5412
    StockLigne = 5462
    for i in range(len(ListeNomNum)):  #Boucle parcourant tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(ListeNomNum[i]), 'r') as f:
            contenu = f.readlines()
            NumeroLigne = 1
            for ligne in contenu:
                mots = ligne.split()  #Séparer les mots dans les lignes
                NumeroMot = 1
                for mot in mots:
                    if mot == "climat":
                        StockLigne = min(StockLigne, NumeroLigne)
                    NumeroMot += 1
                NumeroLigne += 1
        if MinimalLigne >= StockLigne:
            MinimalLigne = StockLigne
            PremierPresidentClimat = ListeNomNum[i]
    return PremierPresidentClimat

def PremierEcologie(L):
    ListeNomNum = extraire_noms_avec_numero(L)
    PremierPresidentEcologie = None
    MinimalLigne = 5412
    StockLigne = 5462
    for i in range(len(ListeNomNum)):  #Boucle parcourant tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(ListeNomNum[i]), 'r') as f:
            contenu = f.readlines()
            NumeroLigne = 1
            for ligne in contenu:
                mots = ligne.split()  #Séparer les mots dans les lignes
                NumeroMot = 1
                for mot in mots:
                    if mot == "écologie":
                        StockLigne = min(StockLigne, NumeroLigne)
                    NumeroMot += 1
                NumeroLigne += 1
        if MinimalLigne >= StockLigne:
            MinimalLigne = StockLigne
            PremierPresidentEcologie = ListeNomNum[i]
    return PremierPresidentEcologie

def find_word_in_corpus(question, files_names):
    l_mot_question=CleanedQuestion(question)
    l_mots_fichiers=[]
    liste_nom_numero = extraire_noms_avec_numero(files_names)  #liste de tout les noms avec numero

    for i in range(len(liste_nom_numero)):  # Boucle permettant de parcourir tous les fichiers, et de calculer chaque tf-idf d'un mot dans un fichier
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r', encoding="utf-8") as f:
            contenu= f.readlines().split()
            l_mots_fichiers.append(contenu)

        for i in range(len(l_mot_question)):
            if l_mot_question[i] not in l_mots_fichiers:
                del(l_mot_question[i])

        return l_mot_question




