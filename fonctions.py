#Importation des bibliothèques autorisées dans le projet
import os
from math import *

#############################################################################################################
# PARTIE 1#
#############################################################################################################

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
            contenu = f.readlines()  # lis le contenu
            for ligne in contenu:  # prends toutes les lignes dans contenu
                for lettre in ligne:  # prendre tous les lettres de chaque ligne
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
        score_IDF = log10(NbTotalDoc / NbDocAvecMot)
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
        matrice_tf_idf.append(L)                #matrice, ligne: fichier, colonne: tf-idf de chaque mot du fichier
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
    MinimalLigne = 5412 #Initie les valeurs très hautes pour qu'elles se fasse écraser par les nouvelles (plus petites)
    StockLigne = 5462
    for i in range(len(ListeNomNum)):  #Boucle parcourant tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(ListeNomNum[i]), 'r') as f:
            contenu = f.readlines() #Lire toutes les lignes du fichier
            NumeroLigne = 1
            for ligne in contenu: #Boucle lisant toutes les lignes du contenu des fichiers
                mots = ligne.split()  #Séparer les mots dans les lignes
                NumeroMot = 1
                for mot in mots: #Boucle parcourant chaque mot dans les lignes
                    if mot == "climat": #Si le mot est climat
                        StockLigne = min(StockLigne, NumeroLigne)
                    NumeroMot += 1
                NumeroLigne += 1
        if MinimalLigne >= StockLigne: #Si ligne minimum est plus grand que ligne stocké alors
            MinimalLigne = StockLigne #Remplacer ligne mini par ligne stocké
            PremierPresidentClimat = ListeNomNum[i]
    return PremierPresidentClimat #Retourne le premier présidant ayant dit climat

def PremierEcologie(L):
    ListeNomNum = extraire_noms_avec_numero(L)
    PremierPresidentEcologie = None
    MinimalLigne = 5412 #Initie les valeurs très hautes pour qu'elles se fasse écraser par les nouvelles (plus petites)
    StockLigne = 5462
    for i in range(len(ListeNomNum)):  #Boucle parcourant tous les fichiers
        with open('cleaned/CleanedNomination_{}.txt'.format(ListeNomNum[i]), 'r') as f:
            contenu = f.readlines() #Lire toutes les lignes du fichier
            NumeroLigne = 1
            for ligne in contenu: #Boucle lisant toutes les lignes du contenu des fichiers
                mots = ligne.split()  #Séparer les mots dans les lignes
                NumeroMot = 1
                for mot in mots:
                    if mot == "écologie": #Si le mot est ecologie
                        StockLigne = min(StockLigne, NumeroLigne)
                    NumeroMot += 1
                NumeroLigne += 1
        if MinimalLigne >= StockLigne: #Si ligne minimum est plus grand que ligne stocké alors
            MinimalLigne = StockLigne #Remplacer ligne mini par ligne stocké
            PremierPresidentEcologie = ListeNomNum[i]
    return PremierPresidentEcologie  #Retourne le premier présidant ayant dit écologie

#############################################################################################################
#PARTIE 2#
#############################################################################################################

def CleanedQuestion(question):
  ponctuation = ['!', ':', ";", '?', '.', ',', '(', ')', '{', '}', '[', ']']  # Liste de caractère devant être supprimé ou remplacé par un espace
  special = ["'", '"', '-']
  question = question.lower()
  for caractere in ponctuation + special: #pour tous les char de la question qui sont dans les deux listes au-dessus
      question = question.replace(caractere, " ") #remplacer un char dans les listes au dessus par un espace
      LQuesClean = question.split()
  return LQuesClean

def find_word_in_corpus(question, files_names):
    l_mot_question=CleanedQuestion(question)
    l_mots_fichiers=[]
    liste_nom_numero = extraire_noms_avec_numero(files_names)  #liste de tout les noms avec numero
    for i in range(len(liste_nom_numero)):  # Boucle permettant de parcourir tous les fichiers, et de calculer chaque tf-idf d'un mot dans un fichier
        with open('cleaned/CleanedNomination_{}.txt'.format(liste_nom_numero[i]), 'r', encoding="utf-8") as f:
            contenu= f.read().split()       #liste contenu de tt les mots des fichiers
            for mot in contenu:             #boucle pour eviter matrice
                l_mots_fichiers.append(mot) #liste mots tt fichiers apprend chaque mot de la liste contenu
    j = int(0)                              #variables j pour eviter de depasser len(l) a cause du del
    for i in range(len(l_mot_question)):
        if l_mot_question[j] not in l_mots_fichiers:    #si le mot de la question n'existe pas dans les fichiers on le supprime
            del(l_mot_question[j])
            j-=1
        j+=1
    return l_mot_question

def TF_IDF_question(question, files_names):
    liste_mots_questions=find_word_in_corpus(question, files_names) #liste mots de la question
    idf=IDF(files_names)   #idf de tt les mots des fichiers
    tf={}
    tf_idf=[]
    tf_idf_tt, mot_tf_tt=TF_IDF(files_names)
    for i in range(len(liste_mots_questions)):  #dico avec repet des mots de la question
        if liste_mots_questions[i] not in tf:
            tf[liste_mots_questions[i]]=1
        else:
            tf[liste_mots_questions[i]]+=1
    for mot in mot_tf_tt:
        if mot in tf:
            tf_idf.append(round(tf[mot]*idf[mot], 2))
        else:
            tf_idf.append(0)
    return tf_idf

def CalculSimilaritéAProduitScalaire(LDoc, LQues):
    ProduitScalaireDocQues = 0
    for i in range(len(LDoc)): #Boucle parcourant les longueurs de la liste TF-IDF de LDoc/LQues (car ils font la meme taille)
        ProduitScalaireDocQues += LDoc[i] * LQues[i] #Utilisation de la formule fournie
    return ProduitScalaireDocQues #Retourne le produit scalaire des 2 listes

def CalculSimilaritéBNormeVecteur(LDocOrQues):
    NormeDocOrQues = 0
    for i in range(len(LDocOrQues)): #Boucle parcourant la longueur de la liste TF-IDF de LDoc ou LQues
        NormeDocOrQues += LDocOrQues[i]**2 #Utilisation de la formule fournie
        NormeDocOrQues = sqrt(NormeDocOrQues) #Utilisation de la formule fournie
    return NormeDocOrQues #Retourne la norme de la liste TF-IDF Doc ou Question

def CalculSimilaritéCFinal(LDoc, LQues):
    ProduitScalaireDocQues = CalculSimilaritéAProduitScalaire(LDoc, LQues) #A) Reprise de la fonction crée au-dessus
    NormeDoc = CalculSimilaritéBNormeVecteur(LDoc) #B) Reprise de la fonction crée au-dessus
    NormeQues = CalculSimilaritéBNormeVecteur(LQues) #B) #Reprise de la fonction crée au-dessus
    if NormeQues == 0 or NormeDoc == 0:
        ScoreSimilarité = 0
    else:
        ScoreSimilarité = ProduitScalaireDocQues / (NormeDoc * NormeQues) #Utilisation de la formule fournie
    return ScoreSimilarité #Retourne le score de similarité de les listes TF-IDF du document et de la question
  
def calcul_doc_plus_pert(question, files_names):
    liste_nom_numero=extraire_noms_avec_numero(files_names)
    matrice_tf_idf, vide =TF_IDF(files_names)
    vecteur_tf_idf_question=TF_IDF_question(question, files_names)
    M_tf_idf=transpose_matrice(matrice_tf_idf)      #transposé de la matrice tf idf pour avoir des lignes qui correspond aux fichiers
    discours=None
    valeur_similarité_max=CalculSimilaritéCFinal(M_tf_idf[0], vecteur_tf_idf_question)  #prend une valeur de similarité et un discours pour pouvoir comparer
    for i in range(1, len(liste_nom_numero)):  # Boucle permettant de parcourir la matrice tf idf par fichier
        valeur_similarité = CalculSimilaritéCFinal(M_tf_idf[i], vecteur_tf_idf_question)
        if valeur_similarité>valeur_similarité_max:
            valeur_similarité_max=valeur_similarité
            discours=liste_nom_numero[i]
    return discours

def contenu_doc_plus_imp(doc_plus_pert): #doc plus important correspond au discours le plus pertinent retourner de calcul_doc_plus_imp
    with open('speeches/Nomination_{}.txt'.format(doc_plus_pert), 'r', encoding="utf-8") as f:
        contenu=f.read()
    return contenu

def TFIDFQuestionPlusElevee(question, files_names):
    tf_idf_doc, liste_mot=TF_IDF(files_names) #on s'en fiche de tf_idf_doc sauf si t'en as besoin apres
    tf_idf = TF_IDF_question(question, files_names)
    valeur_max=tf_idf[0] #valeur random pour pouvoir comparer
    for i in range(len(tf_idf)):
        if tf_idf[i]>valeur_max:
            valeur_max=tf_idf[i]
            position=i
    mot_plus_grand_tf_idf=liste_mot[position]
    son_tf_idf=valeur_max
    return mot_plus_grand_tf_idf

def Reponse(question, files_names):
    ponctuation = ['!', '?', '.']
    doc_plus_pert = calcul_doc_plus_pert(question, files_names)
    contenu1 = contenu_doc_plus_imp(doc_plus_pert)
    contenu= contenu1.replace('\n', ' ')
    mot = TFIDFQuestionPlusElevee(question, files_names)
    liste_contenu=[]
    for car in contenu:
        liste_contenu.append(car)
    FirstOcc = None
    for i in range(len(liste_contenu)):
        if mot[0]==liste_contenu[i]:
            mot_contenu=''
            j=0
            while  liste_contenu[i+j]!=" ":
                mot_contenu+=liste_contenu[i+j]
                j += 1
            if mot==mot_contenu:
                FirstOcc = i
                break
    stop=False
    for i in range(FirstOcc, 0-1, -1):
        if (liste_contenu[i] in ponctuation) and stop==False:
            position_depart=i
            stop=True
    stop=False
    reponse=''
    for i in range(position_depart+1, len(contenu)):
        if not (liste_contenu[i] in ponctuation) and stop==False:
            reponse+=liste_contenu[i]
        else:
            stop=True
    return reponse

def affiner_reponse(question, reponse):
    ponctuation_final = ['!', '?', '.', '...']
    # Liste de propositions non exhaustives
    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr!"
    }
    LA_question=''
    questionnement = question_starters.keys()   #questionnement correspond au début de question (Où? Quand? Comment? etc)
    for mot in questionnement:
        if mot in question:
            LA_question=mot                     #le questionnement present dans la question de l'utilisateur
            reponse_affiner=question_starters[LA_question]  #la reponse affiner prend la reponse correspondant à la question
    if LA_question=='':
        reponse_affiner=''
        dernier_car=''
    for car in reponse:
        for car_f in reponse_affiner:   #prend le dernier caractere de la reponse affiner
            dernier_car = car_f
        if (dernier_car in ponctuation_final) and (97<=ord(car)<=122):  #et si c une ponctuation final et que le caractere actuel de la reponse est en minuscule
            car = chr(ord(car) - 32)    #on la transforme en majuscule
            reponse_affiner += ' ' + car    #on ajoute donc un espace et la lettre majuscule
        else:
            reponse_affiner+=car
    if not car in ponctuation_final:    #si le dernier caractere de la reponse affiner n'est pas une ponctuation, on rajoute un point
        reponse_affiner+='.'
    return reponse_affiner
