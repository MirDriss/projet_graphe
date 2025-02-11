def lire_fichier(fichier): # fonction pour lire le fichier txt

    matrice = []
    compteur = 0
    with open(fichier, 'r') as f: # assure la fermeture du fichier

        matrice.append([0, 0]) # ajout de alpha

        for ligne in f:

            matrice.append(list(map(int, ligne.split())))
            #ligne.split() découpe la ligne en une liste de chaînes de caractères en utilisant les esapces pour separer
            #map(int, ...) convertit chaque élément en entier.
            #list(...) transforme le tout en une liste d'entiers, qu'on ajoute à contraintes

        matrice.append([len(matrice),0,len(matrice)-1]) # ajout de omega
    return matrice



def afficher_matrice(matrice):

    print(len(matrice), "sommets")
    print()
    # Affiche l'en-tête du tableau
    print(f"{'Code':<12}{'Durée':<8}{'Prédécesseurs'}")
    print("-" * 30)  # Ligne de séparation

    # Parcours chaque ligne de la matrice pour afficher les informations
    for ligne in matrice:
        num_tache = ligne[0]
        duree = ligne[1]
        # Si la ligne a plus de 2 éléments, afficher les prédécesseurs, sinon afficher "Aucun"
        if len(ligne) > 2:
            predecesseurs = ", ".join(map(str, ligne[2:]))
        else:
            predecesseurs = "Aucun"

        # Affiche les informations de la ligne formatées
        print(f"{num_tache:<12}{duree:<8}{predecesseurs}")


def negative_duree(matrice): # verifie s'il ya des arcs négatifs

    for ligne in matrice:
        if ( ligne[1] < 0):
            return True
    return False


def dico_successeur(matrice):

    successeur = {}
    pas_de_predecesseur = []
    for i in range(len(matrice)):
        successeur[i] = []
        if(len(matrice[i]) == 2 and matrice[i][0]!= 0): #on récupère les taches qui n'ont pas de préd et ceux qui sont pas alpha --> successeurs de alpha
            pas_de_predecesseur.append(matrice[i][0])



    for ligne in matrice[1:-1]: # pas alpha ni omega
        tache = ligne[0] # je recupere le sommet
        for predecesseur in ligne[2:]: # je recupere les sommets qui sont predecesseurs
            successeur[predecesseur].append(tache)
            #exemple : (2,2,3) --> 2 est un successeur de 3

    for tache,succ in successeur.items():
        if not(succ) and (tache != matrice[-1][0] and tache!= matrice[0][0]):# on regarde ceux qui n'ont pas de successeurs et ceux qui sont pas alpha et omega
            successeur[tache].append(matrice[-1][0]) # successeur devient omega
        if(tache == matrice[0][0]):
            for nb in pas_de_predecesseur:
                successeur[0].append(nb)

        """if succ:
            print("Tache :", tache, " successeur : ", {', '.join(map(str, succ))})
        else:
            print("Tache :", tache, " successeur : Aucun")"""


    return successeur


def dico_fermeture_transitive(matrice):
    dico_succ = dico_successeur(matrice)

    n = len(matrice)

    for i in range(n):   # parcourt tout les sommets
        for sommet in dico_succ :   # parcourt chaque sommets

            nouveaux_succ = set(dico_succ[sommet]) # utilisation du set pour eviter les doublons d'avance

            for sucesseur in dico_succ[sommet]: # je regarde les successeurs du sommet en question

                nouveaux_succ.update(dico_succ[sucesseur]) # j'ajoute les successeurs du successeur

            dico_succ[sommet] = list(nouveaux_succ)

    return dico_succ


def matrice_transitive(matrice):

    dico_matrice = dico_fermeture_transitive(matrice)

    n = len(matrice)
    matrice_trans = [[0] * n for _ in range(n)] # initialisation a 0

    for sommets,succ in dico_matrice.items():
        for tache in succ:
            matrice_trans[sommets][tache] = 1

    return matrice_trans

def afficher_matrice_transitive(matrice):

    MT = matrice_transitive(matrice)

    dico_succ = dico_fermeture_transitive(matrice)

    n = len(MT)

    print("      ", end="")  # Espace pour l'alignement des indices de colonnes

    for i in range(n):
        print(f"{i:^5}", end=" ")  # Largeur fixe pour chaque colonne
    print()  # Nouvelle ligne



    for i in range(n):
        print(f"{i:^5}", end=" ")  # Indice de ligne centré
        for j in range(n):
            if ( MT[i][j] == 0 ):
                print(f"{'0':^5}", end=" ")
            else:
                print(f"{'1':^5}", end=" ")

        print()


#faire une fonction qui fait la matrice des valeurs

def matrice_valeur(matrice):
    matrice_affichage = []
    n = len(matrice)
    dico_succ = dico_successeur(matrice)
    print(dico_succ)
    # Affichage de l'en-tête avec un centrage
    print("    ", end="")  # Espace pour l'alignement des indices de colonnes
    for i in range(n):
        print(f"{i:^5}", end=" ")  # Largeur fixe pour chaque colonne
    print()  # Nouvelle ligne

    # Affichage de la matrice avec centrage
    for i in range(n):
        print(f"{i:^3}", end=" ")  # Indice de ligne centré
        for j in range(n):
            if j in dico_succ[i]:
                print(f"{matrice[i][1]:^5}", end=" ")  # Affichage de la durée
            else:
                print(f"{'*':^5}", end=" ")  # Marque un lien avec une étoile
        print()  # Nouvelle ligne






def circuit(matrice):

    MT = matrice_transitive(matrice)

    for i in range(len(MT)):
        if  MT[i][i] == 1:
            return True

    return False

