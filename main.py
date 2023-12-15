from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers

question=str(input("Saisir une question : "))

print(TF_IDF_question(question, files_names))
