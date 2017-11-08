import networkx as nx
import os 
import seaborn as sns
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

"""
==========
 Le tableau est trié dans un ordre inconnu mais qui est le même pour toutes les scènes
===========
"""

""" On crée un dictionnaire qui associe les noms des persos à leur numéro de noeud """
G1=nx.read_graphml("data\GoT_S05E09_1039.graphml")
dicoNumToNom = nx.get_node_attributes(G1,"label")
dicoNomToNum = {dicoNumToNom[cle]:cle for cle in dicoNumToNom}



liste_graph = []
for element in os.listdir('data')[:2000]:
    liste_graph.append(nx.read_graphml('data\\' + str(element)))
    
    
tableau_centrality = []
for l in liste_graph :
    #l.remove_nodes_from(nx.isolates(l))  ==> Pour enlever les isolates mais on doit les garder pour avoir des 
    """nx.draw_networkx(l,pos=nx.spring_layout(l))  == >  Affichage du graphe de la case liste_graph(l)"""
    tableau_centrality.append(nx.degree_centrality(l))
    
"""   
Test pour voir si on affiche bien seulement les isolates et une seule liste de centrality

print(tableau_centrality[0]) 
print("")
print(tableau_centrality[1]) 
"""

numNoeud = input("Entre le numéro de noeud : ")
numNoeud = "n" + numNoeud
print("Le nom du noeud est : ",numNoeud)

tab =[]
tab.append([x[numNoeud] for x in tableau_centrality])
print(tab[0])
sns.tsplot(tab[0])
plt.savefig("images/n93.jpg")
plt.show()



"""
pourn96 = [x["n96"] for x in tableau_centrality]
print(pourn96)
sns.tsplot(pourn96)
plt.show()
"""



"""
Demander au prof pour seaborn 

sns.set(style = 'darkgrid')
sns.tsplot(data = tab[0], time = "perso?", condition = "ROI", value = "centrality")
"""



"""
def set_extent(pos_, plot_):
    plot_.tick_params(labelbottom="off") 
    plot_.tick_params(labelleft="off") 
    x_values, y_values = zip(*pos_.values()) 
    x_max = max(x_values) 
    y_max = max(y_values) 
    x_min = min(x_values) 
    y_min = min(y_values) 
    x_margin = (x_max - x_min) * 0.1 
    y_margin = (y_max - y_min) * 0.1 
    plot_.set_xlim(x_min - x_margin, x_max + x_margin) 
    plot_.set_ylim(y_min - y_margin, y_max + y_margin)

plot = plt.subplots(2, 2) 
subplots = plot.reshape(1, 4)[0]


for l in liste_graph :
    attributes={}
    attributes["font_size"] = 12 
    attributes["node_size"] = 700
    attributes["width"] = 3 
    attributes["with_labels"] = True
    plot = plt.subplots()
    pos = nx.spring_layout(l)
    nx.draw_networkx(l, pos, **attributes)
    set_extent(pos, plot)
    plt.tight_layout()
    plt.savefig("images/Yolo.pdf") 
    plt.show()

 Demander au prof pour matplotlib.pylot """