from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers

print("Bienvenue dans le pychatbot en developpement ! \n")
print("Nos informations concernent les discords de ces présidents: ")
noms = (extraire_noms_presidents(files_names))
prenom_n = association_prenom(noms)
print_noms(prenom_n)
ConversionMajusculeEnMinuscule(files_names)
del_ponctuations(files_names)
print("\nVoici les fonctionnalités que nous disposons pour le moment : \n")
print("1 - Afficher la liste des mots les moins importants dans le corpus document")
print("2 - Afficher le mot ayant le score TD-IDF le plus élevé")
print("3 - Le mot le plus répéter par un président")
print("4 - Afficher la liste des présidents qui ont parlé de la (Nation) et celui qui l'a répété le plus de fois")
print("5 - Afficher le premier présidant ayant parlé de climat et d'écologie")
print("5 - Afficher le premier présidant ayant parlé d'écologie")
print("6 - Les mots que tous les présidents ont évoqués \n")

print("Pour accéder aux fonctionnalités, veuillez écrire les numéros auxquels elles correspondent")
functionality = input("A quelle fonctionnalité voulez-vous accéder ? ")

if functionality == "1":
    tf_idf, liste_mot = (TF_IDF(files_names))
if functionality == "2":
    print("Le mot avec le tf-idf le plus élevé de tout les discours est: ", tf_idf_max(files_names))
if functionality == "3":
    nom = input("Entrer le nom d'un president dont vous souhaitez connaître le mot le plus répéter dans ses discours : ")
    mot_plus_repet(nom)
if functionality == "4":
    print("Les présidents ayant dit nation sont:", ResultatNation(files_names))
    print("Le président l'ayant le plus dit est:", ResultatNation(files_names)[0])
if functionality == "5":
    print("Le premier président ayant dit climat est", PremierClimat(files_names))
if functionality == "5":
    print("Le premier présidant ayant dit écologie est", PremierEcologie(files_names))
if functionality == "6":
    print("Celui-ci est encore en cours de developpement")







