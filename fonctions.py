import copy
def lire_fichier(fichier):  # fonction pour lire le fichier txt

    matrice = []
    with open(fichier, 'r') as f:  # assure la fermeture du fichier

        matrice.append([0, 0])  # ajout de alpha

        for ligne in f:
            matrice.append(list(map(int, ligne.split())))
            # ligne.split() decoupe la ligne en une liste de chaînes de caracteres en utilisant les esapces pour separer
            # map(int, ...) convertit chaque element en entier.
            # list(...) transforme le tout en une liste d'entiers, qu'on ajoute a contraintes

        for i in range(1, len(matrice)):
            if len(matrice[i]) == 2:
                matrice[i].append(0)

        sommet = [ligne[0] for ligne in matrice[1:]]
        predecesseur_existant = []
        for ligne in matrice[1:]:
            predecesseur_existant.extend(ligne[2:])

        tache_sans_successeurs = []
        for i in sommet:
            if i in predecesseur_existant:
                pass
            else:
                tache_sans_successeurs.append(i)

        tache_omega = len(matrice)
        matrice.append([tache_omega, 0] + tache_sans_successeurs)  # ajout de omega

    return matrice


def nbr_arc(graphe): # Calcule du nombre d'arc dans un graphe
    nbr = -1 # Enlever alpha
    for i in range(len(graphe)):
        nbr += len(graphe[i]) - 2 # Nombre d'élément sur la ligne en enlevant le sommet + la durée
        if (len(graphe[i]) == 2):
            nbr += 1 # Si c'est un sommet source
    return nbr


def afficher_matrice(matrice):
    print()
    # Affiche l'en-tête du tableau
    print(f"{'Sommet':<12}{'Duree':<8}{'Predecesseurs'}")
    print("-" * 30)  # Ligne de separation

    # Parcours chaque ligne de la matrice pour afficher les informations
    for ligne in matrice:
        num_tache = ligne[0]
        duree = ligne[1]
        # Si la ligne a plus de 2 elements, afficher les predecesseurs, sinon afficher "Aucun"
        if len(ligne) > 2:
            predecesseurs = ", ".join(map(str, ligne[2:]))
        else:
            predecesseurs = "Aucun"

        # Affiche les informations de la ligne formatees
        print(f"{num_tache:<12}{duree:<8}{predecesseurs}")
    return


# Affichage du graphe d'ordonnancement
def affichage_graphe_ordonnancement(matrice):
    """
    :affichage:
    nbr sommets
    nbr arcs
    S1 -> S2 = duree
    S2 -> S4 = duree
    S2 -> S6 = duree
    :param matrice:
    :return:
    """
    dico_succ = dico_successeur(matrice)
    print(dico_succ)
    print("\nCreation du graphe d'ordonnancement : ")
    print(len(matrice), "sommets")
    print(nbr_arc(matrice), "arcs")
    for i in range(len(matrice)):
        if dico_succ[i] != []:
            for j in (dico_succ[i]):
                print(i, " -> ", j, " = ", matrice[i][1])
    return


def negative_duree(matrice):  # verifie s'il ya des arcs negatifs
    for ligne in matrice:
        if (ligne[1] < 0):
            print("Le graphe contient au moins un arc a valeur negative.")
            return True
    print("Le graphe ne contient aucun arc a valeur negative.")
    return False


def dico_successeur(matrice):
    successeur = {}
    pas_de_predecesseur = []
    for i in range(len(matrice)):
        successeur[i] = []
        if (len(matrice[i]) == 2 and matrice[i][0] != 0):  # on recupere les taches qui n'ont pas de pred et ceux qui sont pas alpha --> successeurs de alpha
            pas_de_predecesseur.append(matrice[i][0])

    for ligne in matrice[1:-1]:  # pas alpha ni omega
        tache = ligne[0]  # je recupere le sommet
        for predecesseur in ligne[2:]:  # je recupere les sommets qui sont predecesseurs
            successeur[predecesseur].append(tache)
            # exemple : (2,2,3) --> 2 est un successeur de 3

    for tache, succ in successeur.items():
        if not (succ) and (tache != matrice[-1][0] and tache != matrice[0][
            0]):  # on regarde ceux qui n'ont pas de successeurs et ceux qui sont pas alpha et omega
            successeur[tache].append(matrice[-1][0])  # successeur devient omega
        if (tache == matrice[0][0]):
            for nb in pas_de_predecesseur:
                successeur[0].append(nb)

    return successeur


def dico_fermeture_transitive(matrice):
    dico_succ = dico_successeur(matrice)

    n = len(matrice)

    for i in range(n):  # parcourt tout les sommets
        for sommet in dico_succ:  # parcourt chaque sommets

            nouveaux_succ = set(dico_succ[sommet])  # utilisation du set pour eviter les doublons d'avance

            for sucesseur in dico_succ[sommet]:  # je regarde les successeurs du sommet en question

                nouveaux_succ.update(dico_succ[sucesseur])  # j'ajoute les successeurs du successeur

            dico_succ[sommet] = list(nouveaux_succ)

    return dico_succ


def matrice_transitive(matrice):
    dico_matrice = dico_fermeture_transitive(matrice)

    n = len(matrice)
    matrice_trans = [[0] * n for _ in range(n)]  # initialisation a 0

    for sommets, succ in dico_matrice.items():
        for tache in succ:
            matrice_trans[sommets][tache] = 1

    return matrice_trans


def afficher_matrice_transitive(matrice):
    MT = matrice_transitive(matrice)

    n = len(MT)

    print("      ", end="")  # Espace pour l'alignement des indices de colonnes

    for i in range(n):
        print(f"{i:^5}", end=" ")  # Largeur fixe pour chaque colonne
    print()  # Nouvelle ligne

    for i in range(n):
        print(f"{i:^5}", end=" ")  # Indice de ligne centre
        for j in range(n):
            if (MT[i][j] == 0):
                print(f"{'0':^5}", end=" ")
            else:
                print(f"{'1':^5}", end=" ")

        print()


# faire une fonction qui fait la matrice des valeurs

def matrice_valeur(matrice): # Affiche la durees des tache associe aux arcs du graphe
    print("\nMatrice des valeurs")
    matrice_affichage = []
    n = len(matrice)
    dico_succ = dico_successeur(matrice)
    # Affichage de l'en-tête avec un centrage
    print("    ", end="")  # Espace pour l'alignement des indices de colonnes
    for i in range(n):
        print(f"{i:^5}", end=" ")  # Largeur fixe pour chaque colonne
    print()  # Nouvelle ligne

    # Affichage de la matrice avec centrage
    for i in range(n):
        print(f"{i:^3}", end=" ")  # Indice de ligne centre
        for j in range(n):
            if j in dico_succ[i]:
                print(f"{matrice[i][1]:^5}", end=" ")  # Affichage de la duree
            else:
                print(f"{'*':^5}", end=" ")  # Marque un lien avec une etoile
        print()  # Nouvelle ligne


def detecter_circuit_methode_1(matrice):
    MT = matrice_transitive(matrice)

    for i in range(len(MT)):
        if MT[i][i] == 1: # Si un sommet redirige vers lui même, alors circuit
            print("Le graphe contient un circuit.")
            return True
    print("Le graphe ne contient aucun circuit.")
    return False


def detecter_circuit_methode_2(matrice):

    copy_matrice = copy.deepcopy(matrice)

    copy_matrice = sorted(copy_matrice[1:-1], key=len)
    continuer = True

    # Suppressions des sommets Omega et Alpha
    for ligne in copy_matrice:
        predecesseurs = ligne[2:]
        if 0 in predecesseurs:
            ligne.remove(0)


    while continuer:
        continuer = False  # On suppose initialement qu'on ne peut plus continuer
        print(copy_matrice)
        for ligne in copy_matrice[:]:  # on parcourt une copie de la liste pour permettre des suppressions
            sommet = ligne[0]
            predecesseurs = ligne[2:]

            print(f"etude du sommet {sommet}")

            # Si aucun predecesseur ou seulement alpha (0)
            if len(predecesseurs) == 0 or predecesseurs == [0]:
                continuer = True  # On pourra continuer a chercher apres cette suppression
                print(f"\tSommet {sommet} sans predecesseurs (ou seulement alpha)")

                # On enleve le sommet comme predecesseur des autres
                for autre_ligne in copy_matrice:
                    if sommet in autre_ligne[2:]:
                        autre_ligne.remove(sommet)
                        print(f"\t\tSuppression de {sommet} comme predecesseur du sommet {autre_ligne[0]}")

                # On enleve ce sommet de la liste principale
                copy_matrice.remove(ligne)
                print(f"\tSommet {sommet} supprime de la matrice\n")
                break  # On sort pour recommencer le parcours au debut
            else:
                print(f"\tSommet {sommet} possede toujours des predecesseurs : {predecesseurs}, aucune action realisee.\n")

    # Si aucune suppression n'est faite pendant tout le parcours, continuer reste False

    # Apres traitement complet
    if len(copy_matrice) == 0:
        print("Aucun circuit detecte dans le graphe.")
        return False
    else:
        print("Circuit detecte dans le graphe !")
        print("Sommets restants impliques dans un circuit :", [ligne[0] for ligne in copy_matrice])
        return True





def is_graphe_ordonnancement(matrice):
    if negative_duree(matrice):
        print(
            "Le graphe n'est pas un graphe ordonne car il contient au moins un sommet a duree negative.\nOn ne peut pas se servir de celui-ci comme graphe d’ordonnancement.")
        return False

    elif detecter_circuit_methode_2(matrice): # If True, on ne peut pas utiliser ce graphe
        print(
            "Le graphe n'est pas un graphe ordonne.")
        return False
    print("Le graphe est un graphe ordonne, il peut servir de graphe d’ordonnancement.")
    return True


def rang_sommet_matrice(matrice):
    """

    matrice sous forme de tableau a double entree :param matrice:
    dictionnaire avec le rang de chaque sommet :return:
    """
    dico_rang = {}
    dico_succ = dico_successeur(matrice)
    S_actuel = [] # Stocke les sommets de rangs n
    for i in range(len(matrice)):  # detection des Sommets de rangs 0 (Ceux qui n'ont pas de predecesseurs)
        dico_rang[i] = -1
        if (len(matrice[i]) == 2): # S'il y a seulement 2 éléments sur la ligne (nom de la tâche + durée)
            dico_rang[i] = 0
            S_actuel.append(i)
    S_suivant = [] # Stockera les sommets de rangs n + 1
    k = 1 # Rang
    while S_actuel != []: # Tant qu'il n'y a plus de sommet de rangs n + 1 (plus de successeur à nos sommets de rangs n
        for i in range(len(matrice)):
            for j in range(2, len(matrice[i])):
                if (matrice[i][j]) in S_actuel: # Si le sommet est un successeur de d'un des sommets de rang n
                    S_suivant.append(i) # le mettre dans le tableau des rangs n + 1
        for i in S_suivant:
            dico_rang[i] = k
        k += 1 # Augmente le rang
        S_actuel = S_suivant
        S_suivant = []
    return dico_rang # Renvoie le dico



def ranger_ordre_graphe_sommet(graphe):
    dico_sommet = rang_sommet_matrice(graphe)
    graphe_ordonnee = {}

    while dico_sommet:  # Faire temps que le dico n'est pas vide
        sommet_min = min(dico_sommet, key=dico_sommet.get)  # trouver la plus petite valeur et clef
        minimum = dico_sommet[sommet_min]

        graphe_ordonnee[sommet_min] = minimum  # Ajouter le min dans le graphe ordonnee
        del dico_sommet[sommet_min]  # enlever le min du dico

    return graphe_ordonnee


def predecesseur(matrice, indice):
    pred = []
    if len(matrice[indice]) > 2:
        pred = matrice[indice][2:]
    return pred


def graphe_vers_dico(graphe): # donne la matrice sous la forme d'un dico avec {Nom : {durée : X, predecesseur : [S1,S2]}}
    tache = {}
    for i in range(len(graphe)):
        tache[i] = {'duree': graphe[i][1], 'predecesseurs': predecesseur(graphe, i)}
    return tache


def calculer_dates_au_plus_tot(graphe):
    ordre = ranger_ordre_graphe_sommet(graphe)
    # Recuperer le graphe sous forme de dictionnaire
    taches = graphe_vers_dico(graphe)
    # Initialisation des dates au plus tot
    dates_au_plus_tot = {tache: 0 for tache in taches}  # On commence toutes les dates a 0

    # Parcours des tâches dans l'ordre croisant des rangs
    for tache in ordre:
        # Pour chaque predecesseur, on calcule la date de fin et on met à jour la date de debut
        for pred in taches[tache]['predecesseurs']:
            # La tâche peut commencer une fois que toutes ses predecesseurs sont terminees
            dates_au_plus_tot[tache] = max(dates_au_plus_tot[tache], dates_au_plus_tot[pred] + taches[pred]['duree'])

    return dates_au_plus_tot


def calculer_dates_au_plus_tard(matrice):
    ordre = ranger_ordre_graphe_sommet(matrice)

    # Recuperer le graphe sous forme de dictionnaire
    tasks = graphe_vers_dico(matrice)
    dates_au_plus_tot = calculer_dates_au_plus_tot(matrice)
    successeurs = dico_successeur(matrice)

    duree_projet = max(dates_au_plus_tot.values())

    #initialisation de date au plus tard à l'aide de la date au projet. Permet à omega d'avoir la date de fin
    dates_au_plus_tard = {task: duree_projet for task in tasks}

    #on parcourt dans le sens décroissant des rangs
    for task in reversed(ordre):
        # on verifie si on est sur omega
        if not successeurs[task]:
            dates_au_plus_tard[task] = duree_projet
        # il faut respecter la contrainte de temps la plus importante. Soit la plus petite valeur.
        else:
            date_min = min(dates_au_plus_tard[succ] for succ in successeurs[task])
            dates_au_plus_tard[task] = date_min - tasks[task]['duree']
    return dates_au_plus_tard


def afficher_dates_au_plus_tot(dates_au_plus_tot): # Afficher les dates au plus tôt de chaque sommet
    for tache, date in dates_au_plus_tot.items():
        print(f"Tâche {tache} peut commencer au plus tot a la date {date}.")
    return


def afficher_dates_au_plus_tard(dates_au_plus_tot): # Afficher les dates au plus tard de chaque sommet
    for tache, date in dates_au_plus_tot.items():
        print(f"Tâche {tache} peut commencer au plus tard a la date {date}.")
    return


def afficher_rang_sommets(dico):
    print("Les rangs de chaque sommets sont les suivants :")
    print(f"{'Code':<12}{'Rang':<8}")
    print("-" * 16)  # Ligne de separation
    for i in range(len(dico)):
        print(i, "\t" * 3, dico[i])
    return


def selection_fichier(): # Sélection d'un fichier
    fichier = "Graphe/" # Ouvre le dossier contenant les graphes
    print("Veuillez choisir la table que vous souhaitez (1-14) ?")
    choix = int(input(">>> ")) # Selection d'un fichier entre 1 et 14
    while (int(choix) < 1 or int(choix) > 14): # Le choix de l'utilisateur est-il compris entre 1 et 14
        print(
            "La valeur que vous avez choisi '" + str(choix) + "' n'est pas acceptable. \nVeuillez choisir une nouvelle valeur ?")
        choix = input(">>> ")
    fichier += "table " + str(choix) + ".txt" # le chemin de notre fichier
    return fichier


def calculer_marges_arcs(matrice):
    """
    Calcule la marge pour chaque arc (i -> j) de la matrice.
    Pour un arc allant du prédécesseur i vers le sommet j,
    la marge est définie par :

        marge = dates_tard[j] - (dates_tot[i] + durée(i))

    où durée(i) est la durée associée au sommet i.
    """

    dates_tot = calculer_dates_au_plus_tot(matrice)
    dates_tard = calculer_dates_au_plus_tard(matrice)
    # Création d'un dictionnaire pour accéder rapidement à la durée de chaque sommet
    duree = {tache[0]: tache[1] for tache in matrice}

    marges = []
    for tache in matrice:
        sommet = tache[0]  # sommet d'arrivée
        predecesseurs = tache[2:]  # liste des prédécesseurs de j
        for pred in predecesseurs:
            marge = dates_tard[sommet] - (dates_tot[pred] + duree[pred])
            marges.append(((pred, sommet), marge))
    return marges


def chemins_critiques(matrice):
    """
    Calcule les chemins critiques à partir de la matrice.

    On part du nœud 0 et on recherche tous les chemins menant
    au nœud final (matrice[-1][0]) en ne suivant que les arcs dont la marge est 0.

    La fonction calculer_marges_arcs(matrice) est utilisée pour obtenir les marges.
    """
    # Calcul des marges sur chaque arc
    marges = calculer_marges_arcs(matrice)

    # Construction d'un dictionnaire de successeurs critiques :
    # Pour chaque arc (i -> j) avec marge == 0, on ajoute j comme successeur de i.
    successeurs_critique = {}
    for (i, j), marge in marges:
        if marge == 0:
            successeurs_critique.setdefault(i, []).append(j)

    # On considère que le nœud final est le premier élément de la dernière tâche de la matrice
    final_node = matrice[-1][0]
    chemins = []

    # Fonction récursive pour explorer le graphe des arcs critiques
    def explorer(chemin):
        courant = chemin[-1]
        # Si on a atteint le noeuud final, on ajoute le chemin trouvé
        if courant == final_node:
            chemins.append(chemin)
            return
        # Sinon on parcourt tous les successeurs critiques du noeud courant
        for succ in successeurs_critique.get(courant, []):
            explorer(chemin + [succ])

    # Démarrage de l'exploration depuis le noeud 0
    explorer([0])
    return chemins