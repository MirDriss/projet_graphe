from fonctions import *
from colorama import init, Fore
import time
import sys
from contextlib import redirect_stdout



class Tee:
    def __init__(self, *outputs):
        self.outputs = outputs

    def write(self, message):
        for output in self.outputs:
            output.write(message)

    def flush(self):
        for output in self.outputs:
            output.flush()



init(autoreset=True)

def menu():
    header = f"""{Fore.BLUE}
    ╔═╗ ╦═╗ ╔═╗ ╔═╗ ╦ ╦ ╔═╗ ╔═╗
    ║   ╠╦╝ ╠═╣ ╠═╝ ╠═╣ ║╣  ╚═╗
    ╚═╝ ╩╚═ ╩ ╩ ╩   ╩ ╩ ╚═╝ ╚═╝  by Braquemart, Dos Santos, H'lali, Mir, Vazquez
    """

    continuer = True
    step = "select"
    display = "matrice"

    while continuer:
        print("\033[H\033[J", end="")
        print(header)

        if step == "select":
            fichier = selection_fichier()
            matrice = lire_fichier(fichier)
            step = "selected"

        if step == "selected":
            if display == "matrice":
                print(f"""{Fore.BLUE}Graph {fichier.split("/")[-1]} séléctionné :""")
                afficher_matrice(matrice)
            elif display == "is_graphe_ordonnancement":
                print(f"""{Fore.BLUE}Verification si le graph {fichier.split("/")[-1]} est il ordonnancable :""")
                is_graphe_ordonnancement(matrice)
            elif display == "afficher_rang_sommets":
                print(f"""{Fore.BLUE}Graph {fichier.split("/")[-1]} séléctionné:""")
                afficher_rang_sommets(rang_sommet_matrice(matrice))


            print(f"""{Fore.BLUE}\n\t MENU""")
            print("1 - Sauvegardez le graphe")
            print("2 - Choisir un autre graphe")
            print("3 - Affihcer la matrice correspondante au graphe")
            print("4 - Verfier si le graphe peut être ordonnancé ")
            print("5 - Afficher les rangs des sommets ")
            print("6 - Executer le programme en entier avec les traces d'éxecutions")
            choix = input(f"""{Fore.BLUE}>>> """)
            if (choix == "1"):
                print(f"""{Fore.RED}Ca marche pas encore désolé""")
                time.sleep(3)
            elif choix == "2":
                step = "select"
            elif choix == "3":
                display = "matrice"
            elif choix == "4":
                display = "is_graphe_ordonnancement"
            elif choix == "5":
                display = "afficher_rang_sommets"
            elif choix == "6":
                fichier_to_write = "Trace/trace_" + fichier.split("/")[-1]
                print("Ecriture dans ", fichier_to_write);
                with open(fichier_to_write, "w") as logfile:
                    sys.stdout = Tee(sys.__stdout__, logfile)
                    print("\n\n--- Étape : Vérification du graphe ---")
                    if is_graphe_ordonnancement(matrice):
                        print(f"""{Fore.BLUE}\n--- Étape : Calcul des rangs ---""")
                        rangs = rang_sommet_matrice(matrice)
                        afficher_rang_sommets(rangs)

                        print(f"""{Fore.BLUE}\n--- Étape : Calendrier au plus tôt ---""")
                        dates_tot = calculer_dates_au_plus_tot(matrice)
                        afficher_dates_au_plus_tot(dates_tot)

                        print(f"""{Fore.BLUE}\n--- Étape : Calendrier au plus tard ---""")
                        dates_tard = calculer_dates_au_plus_tard(matrice)
                        afficher_dates_au_plus_tard(dates_tard)

                        print(f"""{Fore.BLUE}\n--- Étape : Calcul des marges ---""")
                        for tache in dates_tot:
                            marge = dates_tard[tache] - dates_tot[tache]
                            print(f"Tâche {tache} a une marge de {marge}.")

                        print(f"""{Fore.BLUE}\n--- Étape : Chemins critiques ---""")
                        print("Chemin(s) critique(s) :")
                        for tache in dates_tot:
                            if dates_tot[tache] == dates_tard[tache]:
                                print(f"La tâche {tache} est critique.")
                    else:
                        print(f"""{Fore.BLUE}Ce graphe ne peut pas être utilisé pour l'ordonnancement.""")
                    sys.stdout = sys.__stdout__

                choix = input("\nVoulez-vous tester un autre tableau de contraintes (oui/non) ? ")
                continuer = choix
                if continuer == "oui":
                    step = "select"

    print("\nFin du programme.")


if __name__ == '__main__':
    menu()