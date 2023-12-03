from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers

noms = (extraire_noms_presidents(files_names))
prenom_n = association_prenom(noms)
print_noms(prenom_n)
ConversionMajusculeEnMinuscule(files_names)
del_ponctuations(files_names)


tf_idf, liste_mot = (TF_IDF(files_names))

print("Le mot avec le tf-idf le plus élevé de tout les discours est: ", tf_idf_max(files_names))



print("Les présidents ayant dit Nation sont:", ResultatNation(files_names))
print("Le président l'ayant le plus dit est:", ResultatNation(files_names)[0])