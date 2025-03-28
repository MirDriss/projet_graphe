def lire_fichier(fichier):  # fonction pour lire le fichier txt

    matrice = []
    with open(fichier, 'r') as f:  # assure la fermeture du fichier

        matrice.append([0, 0])  # ajout de alpha

        for ligne in f:
            matrice.append(list(map(int, ligne.split())))
            # ligne.split() découpe la ligne en une liste de chaînes de caractères en utilisant les esapces pour separer
            # map(int, ...) convertit chaque élément en entier.
            # list(...) transforme le tout en une liste d'entiers, qu'on ajoute à contraintes

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


def nbr_arc(graphe):
    nbr = -1
    for i in range(len(graphe)):
        nbr += len(graphe[i]) - 2
        if (len(graphe[i]) == 2):
            nbr += 1
    return nbr


def afficher_matrice(matrice):
    print()
    # Affiche l'en-tête du tableau
    print(f"{'Sommet':<12}{'Durée':<8}{'Prédécesseurs'}")
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
    print("\nCréation du graphe d'ordonnancement : ")
    print(len(matrice), "sommets")
    print(nbr_arc(matrice), "arcs")
    for i in range(len(matrice)):
        if dico_succ[i] != []:
            for j in (dico_succ[i]):
                print(i, " -> ", j, " = ", matrice[i][1])
    return


def negative_duree(matrice):  # verifie s'il ya des arcs négatifs
    for ligne in matrice:
        if (ligne[1] < 0):
            print("Le graphe contient au moins un arc à valeur négative.")
            return True
    print("Le graphe ne contient aucun arc à valeur négative.")
    return False


def dico_successeur(matrice):
    successeur = {}
    pas_de_predecesseur = []
    for i in range(len(matrice)):
        successeur[i] = []
        if (len(matrice[i]) == 2 and matrice[i][0] != 0):  # on récupère les taches qui n'ont pas de préd et ceux qui sont pas alpha --> successeurs de alpha
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
        print(f"{i:^5}", end=" ")  # Indice de ligne centré
        for j in range(n):
            if (MT[i][j] == 0):
                print(f"{'0':^5}", end=" ")
            else:
                print(f"{'1':^5}", end=" ")

        print()


# faire une fonction qui fait la matrice des valeurs

def matrice_valeur(matrice): # Affiche la durées des tache associé aux arcs du graphe
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
        print(f"{i:^3}", end=" ")  # Indice de ligne centré
        for j in range(n):
            if j in dico_succ[i]:
                print(f"{matrice[i][1]:^5}", end=" ")  # Affichage de la durée
            else:
                print(f"{'*':^5}", end=" ")  # Marque un lien avec une étoile
        print()  # Nouvelle ligne


def detecter_circuit_methode_1(matrice):
    MT = matrice_transitive(matrice)

    for i in range(len(MT)):
        if MT[i][i] == 1: # Si un sommet redirige vers lui même, alors circuit
            print("Le graphe contient un circuit.")
            return True
    print("Le graphe ne contient aucun circuit.")
    return False


def detecter_circuit_methode_3(matrice):
    copy_matrice = sorted(matrice[1:-1], key=len)
    continuer = True

    while continuer:
        continuer = False  # On suppose initialement qu'on ne peut plus continuer
        for ligne in copy_matrice[:]:  # on parcourt une copie de la liste pour permettre des suppressions
            sommet = ligne[0]
            predecesseurs = ligne[2:]

            print(f"Étude du sommet {sommet}")

            # Si aucun prédécesseur ou seulement alpha (0)
            if len(predecesseurs) == 0 or predecesseurs == [0]:
                continuer = True  # On pourra continuer à chercher après cette suppression
                print(f"\tSommet {sommet} sans prédécesseurs (ou seulement alpha)")

                # On enlève le sommet comme prédécesseur des autres
                for autre_ligne in copy_matrice:
                    if sommet in autre_ligne[2:]:
                        autre_ligne.remove(sommet)
                        print(f"\t\tSuppression de {sommet} comme prédécesseur du sommet {autre_ligne[0]}")

                # On enlève ce sommet de la liste principale
                copy_matrice.remove(ligne)
                print(f"\tSommet {sommet} supprimé de la matrice\n")
                break  # On sort pour recommencer le parcours au début
            else:
                print(f"\tSommet {sommet} possède toujours des prédécesseurs : {predecesseurs}, aucune action réalisée.\n")

    # Si aucune suppression n'est faite pendant tout le parcours, continuer reste False

    # Après traitement complet
    if len(copy_matrice) == 0:
        print("Aucun circuit détecté dans le graphe.")
        return False
    else:
        print("Circuit détecté dans le graphe !")
        print("Sommets restants impliqués dans un circuit :", [ligne[0] for ligne in copy_matrice])
        return True




def detecter_circuit_methode_2(matrice):
    changement = True
    copy_matrice = sorted(matrice[1:-1], key=len) # Tri pour rapidement reperer les sommets sans predecesseur


    while changement:
        if (len(copy_matrice) != 0):
            ligne = copy_matrice[0]
            print("Etude du sommet " + str(ligne[0]))
            if (len(ligne) < 3 or ligne[2]==0):  # on vérifie si le sommet n'a pas de predecesseur
                sommet = ligne[0]  # on récupère le sommet qui est sans predecesseur
                print("avant suppression de la ligne :", copy_matrice)
                copy_matrice.pop(copy_matrice.index(ligne))  # on supprime la ligne ou y a le sommet en question
                print("apres suppression de la ligne :", copy_matrice)
                for i in range(
                        len(copy_matrice)):  # on enlève là où le sommet apparait comme prédecesseur pour les autres sommets
                    if sommet in copy_matrice[i][2:]:
                        print("liste des predecesseur", copy_matrice[i][2:])
                        print("sommet à supprimer", sommet)
                        print()
                        copy_matrice[i].remove(sommet)

            else:
                changement = False
        else:

            changement = False
            print(copy_matrice)

    if (len(copy_matrice) == 0):
        print("Il n'y pas de circuit")
        return False

    print("Il y un circuit")
    return True


def is_graphe_ordonnancement(matrice):
    if negative_duree(matrice):
        print(
            "Le graphe n'est pas un graphe ordonné car il contient au moins un sommet à durée négative.\nOn ne peut pas se servir de celui-ci comme graphe d’ordonnancement.")
        return False

    elif detecter_circuit_methode_3(matrice): # If True, on ne peut pas utiliser ce graphe
        print(
            "Le graphe n'est pas un graphe ordonné.")
        return False
    print("Le graphe est un graphe ordonné, il peut servir de graphe d’ordonnancement.")
    return True


def rang_sommet_matrice(matrice):
    """

    matrice sous forme de tableau à double entrée :param matrice:
    dictionnaire avec le rang de chaque sommet :return:
    """
    dico_rang = {}
    dico_succ = dico_successeur(matrice)
    S_actuel = []
    for i in range(len(matrice)):  # détection des Sommets de rangs 0 (Ceux qui n'ont pas de prédécesseurs)
        dico_rang[i] = -1
        if (len(matrice[i]) == 2):
            dico_rang[i] = 0
            S_actuel.append(i)
    S_suivant = []
    k = 1
    while S_actuel != []:
        for i in range(len(matrice)):
            for j in range(2, len(matrice[i])):
                if (matrice[i][j]) in S_actuel:
                    S_suivant.append(i)
        for i in S_suivant:
            dico_rang[i] = k
        k += 1
        S_actuel = S_suivant
        S_suivant = []
    return dico_rang


def rang_sommet_matrice2(matrice):
    dico_rang = {i: -1 for i in range(len(matrice))}
    k = 0
    rang_restant = [ligne[0] for ligne in matrice]

    for ligne in matrice:
        if (len(ligne) == 2):
            dico_rang[ligne[0]] = k
            rang_restant.remove(ligne[0])
    k += 1

    while rang_restant != []:
        nouveaux_ranges = []

        for i in rang_restant:
            if all(j not in rang_restant for j in matrice[i][2:]):
                dico_rang[i] = k
                nouveaux_ranges.append(i)

        for i in nouveaux_ranges:
            rang_restant.remove(i)

        k += 1

        return dico_rang


def ranger_ordre_graphe_sommet(graphe):
    dico_sommet = rang_sommet_matrice(graphe)
    graphe_ordonnee = {}

    while dico_sommet:  # Faire temps que le dico n'est pas vide
        sommet_min = min(dico_sommet, key=dico_sommet.get)  # trouver la plus petite valeur et clef
        minimum = dico_sommet[sommet_min]

        graphe_ordonnee[sommet_min] = minimum  # Ajouter le min dans le graphe ordonnée
        del dico_sommet[sommet_min]  # enlever le min du dico

    return graphe_ordonnee


def predecesseur(matrice, indice):
    pred = []
    if len(matrice[indice]) > 2:
        pred = matrice[indice][2:]
    return pred


def graphe_vers_dico(graphe):
    tache = {}
    for i in range(len(graphe)):
        tache[i] = {'duree': graphe[i][1], 'predecesseurs': predecesseur(graphe, i)}
    return tache


def calculer_dates_au_plus_tot(graphe):
    # Récupérer le graphe sous forme de dictionnaire
    taches = graphe_vers_dico(graphe)
    # Initialisation des dates au plus tôt
    dates_au_plus_tot = {tache: 0 for tache in taches}  # On commence toutes les dates à 0

    # Parcours des tâches dans l'ordre topologique
    for tache in taches:
        # Pour chaque prédécesseur, on calcule la date de fin et on met à jour la date de début
        for pred in taches[tache]['predecesseurs']:
            # La tâche peut commencer une fois que toutes ses prédécesseurs sont terminées
            dates_au_plus_tot[tache] = max(dates_au_plus_tot[tache], dates_au_plus_tot[pred] + taches[pred]['duree'])

    return dates_au_plus_tot


def calculer_dates_au_plus_tard(matrice):
    tasks = graphe_vers_dico(matrice)
    dates_au_plus_tot = calculer_dates_au_plus_tot(matrice)
    successeurs = dico_successeur(matrice)

    duree_projet = max(dates_au_plus_tot.values())

    dates_au_plus_tard = {task: duree_projet for task in tasks}

    for task in reversed(tasks):
        if not successeurs[task]:
            dates_au_plus_tard[task] = duree_projet
        else:
            date_min = min(dates_au_plus_tard[succ] for succ in successeurs[task])
            dates_au_plus_tard[task] = date_min - tasks[task]['duree']
    return dates_au_plus_tard


def afficher_dates_au_plus_tot(dates_au_plus_tot):
    for tache, date in dates_au_plus_tot.items():
        print(f"Tâche {tache} peut commencer au plus tôt à la date {date}.")
    return


def afficher_dates_au_plus_tard(dates_au_plus_tot):
    for tache, date in dates_au_plus_tot.items():
        print(f"Tâche {tache} peut commencer au plus tard à la date {date}.")
    return


def afficher_rang_sommets(dico):
    print("Les rangs de chaque sommets sont les suivants :")
    print(f"{'Code':<12}{'Rang':<8}")
    print("-" * 16)  # Ligne de séparation
    for i in range(len(dico)):
        print(i, "\t" * 3, dico[i])
    return


def selection_fichier():
    fichier = "Graphe/"
    print("Veuillez choisir la table que vous souhaitez (0-15) ?")
    choix = int(input(">>> "))
    while (int(choix) < 0 or int(choix) > 15):
        print(
            "La valeur que vous avez choisis '" + choix + "' n'est pas acceptable. \nVeuillez choisisr une nouvelle valeur ?")
        choix = input(">>> ")
    fichier += "table " + str(choix) + ".txt"
    return fichier


def afficher_chemin_critique():
    pass