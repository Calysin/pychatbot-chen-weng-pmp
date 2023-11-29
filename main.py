from fonctions import *


# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers

noms = files_names
print(extraire_noms_presidents(noms))