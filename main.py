from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers

print("Bienvenue dans le pychatbot ! \n")
print("Nos informations concernent les discours de ces présidents: ")
noms = (extraire_noms_presidents(files_names))
prenom_n = association_prenom(noms)
print_noms(prenom_n)
ConversionMajusculeEnMinuscule(files_names)
del_ponctuations(files_names)
print("\nVoici les fonctionnalités que nous disposons pour le moment : \n")
menu = print("1 - Afficher la liste des mots les moins importants dans le corpus document \n"
             "2 - Afficher le mot ayant le score TD-IDF le plus élevé \n"
             "3 - Afficher le mot le plus répéter par un président\n"
             "4 - Afficher la liste des présidents qui ont parlé de la (Nation) et celui qui l'a répété le plus de fois\n"
             "5 - Afficher le premier présidant ayant parlé de climat et d'écologie\n"
             "6 - Afficher les mots que tous les présidents ont évoqués \n"
             "7 - Notre PyChatBot")
print("Pour accéder aux fonctionnalités, veuillez écrire les numéros auxquels elles correspondent")

recommencer=1
while recommencer==1:
    functionality = input("A quelle fonctionnalité voulez-vous accéder ? ")
    if functionality == "1":
        print("Les mots les moins importants dans les textes sont: ")
        print(tf_idf_0(files_names))
    elif functionality == "2":
        print("Le mot avec le tf-idf le plus élevé de tout les discours est: ", tf_idf_max(files_names))
    elif functionality == "3":
        print("Merci d'écrire le nom du président avec une majuscule au début")
        nom = input("Entrez le nom d'un président dont vous souhaitez connaître le mot le plus souvent répété dans ses discours: ")
        mot_plus_repet(nom, files_names)
    elif functionality == "4":
        print("Les présidents ayant dit nation sont:", ResultatNation(files_names))
        print("Le président l'ayant le plus dit est:", ResultatNation(files_names)[0])
    elif functionality == "5":
        print("Le premier président ayant dit climat est", PremierClimat(files_names))
        print("Le premier présidant ayant dit écologie est", PremierEcologie(files_names))
    elif functionality == "6":
        print("Celui-ci est encore en cours de developpement")
    elif functionality >= "7":
        Question = input("Donnez moi votre question ? ")
        print(Reponse(Question, files_names))

    print("Souhaitez vous utiliser d'autre fonctionnalité?")
    recommencer=int(input("0 : Non\n"
                          "1 : Oui\n"))