from fonctions import *

fichier = "graphe.txt"  # Nom du fichier à lire
matrice = lire_fichier(fichier)
ordo = afficher_matrice(matrice)

print(detecter_circuit_methode_3(matrice))

# matrice_valeur(matrice)





"""
run = True

while run: # Tant que l’utilisateur décide de tester un tableau de contraintes faire
    fichier_txt = selection_fichier() # Choisir le tableau de contraintes à traiter
    matrice = lire_fichier(fichier_txt) # Lire le tableau de contraintes sur fichier et le stocker en mémoire
    afficher_matrice(matrice)
    input("Appuyer sur Entrée ...")
    print("\n\n")

    affichage_graphe_ordonnancement(matrice) # Création de la matrice correspondant au graphe représentant le tableau de contraintes
    if (is_graphe_ordonnancement(matrice)): # Vérification des propriétés nécessaires pour que ce graphe soit un graphe d’ordonnancement
        input("Appuyer sur Entrée ...")
        print("\n\n")
        afficher_rang_sommets(rang_sommet_matrice(matrice)) # Calculer les rangs des sommets et les afficher

        # Afficher les dates au plus tôt et au plus tard
        calculer_dates_au_plus_tot(matrice)
        calculer_dates_au_plus_tard(matrice)

        # Calculer les marges et les afficher
        # On ne l'a toujours pas fait

        # Affichage des chamins critiques
        # On ne l'a pas encore fait


    else:
        print("Le tableau de contraintes ne permet pas que le graphe associé soit un graphe d’ordonnancement.")
    input("Appuyer sur Entrée ...")
    print("\n\n")


    print("Voulez-vous tester un nouveau tableau de contraiantes ? (y-n)") # Proposer à l’utilisateur de changer de tableau de contraintes
    choix = input(">>> ")
    while choix != "n" and choix != "y":
        print("La réponse n'est pas reconnue. Voulez-vous tester un nouveau tableau de contraiantes ? (y-n)\nTapez 'y' pour oui ou 'n' pour non.")
        choix = input(">>> ")
    if choix == "n":
        run = False
"""





"""
print("Au plus tot : ")
print(calculer_dates_au_plus_tot(matrice))
afficher_dates_au_plus_tot(calculer_dates_au_plus_tot(matrice))
print("Au plus tard : ")
print(calculer_dates_au_plus_tard(matrice))
afficher_dates_au_plus_tard(calculer_dates_au_plus_tard(matrice))
# ranger_ordre_graphe_sommet(matrice)
#boolean = negative_duree(matrice)

#print()



matrice_valeur(matrice)

dico_transitif = dico_fermeture_transitive(matrice)


print(dico_transitif)

MT = matrice_transitive(matrice)

afficher_matrice_transitive(matrice)
"""



