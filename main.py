from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers


#question=str(input("Saisir une question : "))

question=str(input("Saisir la question: "))
reponse=str(input("Saisir la reponse: "))

print(affiner_reponse(question, reponse))

#print(TF_IDF_question(question, files_names))
