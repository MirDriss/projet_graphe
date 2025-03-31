from fonctions import *

fichier = selection_fichier()
matrice = lire_fichier(fichier)
print(matrice)

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
    print(duree)

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

chemin = chemins_critiques(matrice)
print("marge : ", chemin)