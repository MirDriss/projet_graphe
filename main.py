from fonctions import *

fichier = "graphe.txt"  # Nom du fichier à lire
matrice = lire_fichier(fichier)
ordo = afficher_matrice(matrice)


#boolean = negative_duree(matrice)

#print()





matrice_valeur(matrice)

dico_transitif = dico_fermeture_transitive(matrice)

print("c moi")

print(dico_transitif)

MT = matrice_transitive(matrice)

afficher_matrice(MT)

print(circuit(MT))
