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

x, y = (TF_IDF(files_names))

i=0
for ligne in x:
    print(y[i], end="")
    print(ligne)
    i+=1

print(tf_idf_max(files_names))