import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

# Définition de la matrice
matrice = [
    [0, 0],
    [1, 9, 0],
    [2, 2, 0],
    [3, 3, 2],
    [4, 5, 1],
    [5, 2, 1, 4],
    [6, 2, 5],
    [7, 0, 3, 6]
]

# Création d'un graphe orienté
G = nx.DiGraph()

# Ajout des sommets et des arêtes
for ligne in matrice:
    sommet = ligne[0]
    cout = ligne[1]
    G.add_node(sommet, cost=cout)
    for pred in ligne[2:]:
        G.add_edge(pred, sommet, weight=cout)

# Utilisation de Kamada-Kawai layout pour une meilleure répartition
pos = nx.kamada_kawai_layout(G)

# Dessiner les nœuds, arêtes et labels
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=600)
nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
nx.draw_networkx_labels(G, pos)

# Affichage des poids sur les arêtes
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Graphe avec Kamada-Kawai layout")
plt.axis('off')
plt.show()
