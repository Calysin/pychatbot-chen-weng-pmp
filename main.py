from fonctions import *

# Call of the function
directory = "./speeches"
files_names = list_of_files(directory, "txt")
#fils names correspond a une liste contenant tous les noms de fichiers


#question=str(input("Saisir une question : "))


M=[[1, 8, 64, 97, 14, 22, 78, 55],
   [2, 8, 64, 97, 14, 22, 78, 55],
   [3, 8, 64, 97, 14, 22, 78, 55],
   [4, 8, 64, 97, 14, 22, 78, 55],
   [5, 8, 64, 97, 14, 22, 78, 55],
   [6, 8, 64, 97, 14, 22, 78, 55],
   [7, 8, 64, 97, 14, 22, 78, 55],
   [8, 8, 64, 97, 14, 22, 78, 55],
   [9, 8, 64, 97, 14, 22, 78, 55],
   [10, 8, 64, 97, 14, 22, 78, 55],
   [11, 8, 64, 97, 14, 22, 78, 55],
   [12, 8, 64, 97, 14, 22, 78, 55]]

transpose_M=(transpose_matrice(M))
for ligne in transpose_M:
    print(ligne)

transpose2_M=(transpose_matrice(transpose_M))
for ligne in transpose2_M:
    print(ligne)

#print(TF_IDF_question(question, files_names))
