from fonctions import *

fichier = "graphe.txt"  # Nom du fichier à lire
matrice = lire_fichier(fichier)
ordo = afficher_matrice(matrice)


print(calculer_dates_au_plus_tot(matrice))
# ranger_ordre_graphe_sommet(matrice)
#boolean = negative_duree(matrice)

#print()



"""
matrice_valeur(matrice)

dico_transitif = dico_fermeture_transitive(matrice)


print(dico_transitif)

MT = matrice_transitive(matrice)

afficher_matrice_transitive(matrice)
"""
# print(detecter_circuit_methode_2(matrice))