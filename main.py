from fonctions import *

fichier = "graphe.txt"
matrice = lire_fichier(fichier)


def chemins_critiques(matrice):
    print("=== RECHERCHE DE CHEMINS CRITIQUES ===")
    succ = dico_successeur(matrice)
    marges = calcul_marge(matrice)

    solutions = [[0]]
    level = 0

    # Boucle de calcul des chemins
    while level < len(solutions):
        new_extensions = 0
        current_length = len(solutions)
        print(f"\n--- Niveau {level} ---")
        for i in range(level, current_length):
            sommet = solutions[i][-1]
            successeurs = succ[sommet]
            print(f"[Chemin {i}] Sommet actuel : {sommet} | Successeurs : {successeurs}")
            for successeur in successeurs:
                if marges[successeur] == 0:
                    new_extensions += 1
                    nouvelle_solution = solutions[i] + [successeur]
                    print(f"   => Extension : {nouvelle_solution}")
                    solutions.append(nouvelle_solution)
        if new_extensions == 0:
            print("Aucune extension possible à ce niveau. Fin de la recherche.")
            break
        level = current_length

    # Affichage de l'ensemble des chemins trouvés
    print("\n=== Chemins complets trouvés ===")
    for sol in solutions:
        print(sol)

    # Filtrer les solutions qui atteignent le dernier sommet (on suppose ici que le dernier sommet est indiqué par le premier élément du dernier sous-tableau)
    chemins_critiques = [sol for sol in solutions if sol[-1] == matrice[-1][0]]

    print("\n=== Chemins critiques (atteignant le dernier sommet) ===")
    for sol in chemins_critiques:
        print(sol)

    return chemins_critiques


def chemins_critiques(matrice):
    marge = calcul_marge(matrice)
    successeurs = dico_successeur(matrice)
    chemins = []

    def explorer(chemin):
        dernier = chemin[-1]
        if successeurs[dernier] == []:
            chemins.append(chemin)
            return
        for succ in successeurs[dernier]:
            if marge.get(succ, -1) == 0:
                explorer(chemin + [succ])

    if marge.get(0, -1) == 0:
        explorer([0])

    return chemins
