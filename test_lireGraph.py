import networkx as nx
import os 
import seaborn as sns
import matplotlib.pyplot as plt
#from networkx.drawing.nx_agraph import graphviz_layout



def type_centralite_voulu(numNoeud) :
    
    liste = str(input("Entrez la(les) centralite(s) voulue(s) :  - d pour degree   - c pour closeness   - p pour pagerank   - b pour betweeness   "))
    i = 0
    tab =[]

    
    if 'd' in liste:
        tab.append([x[numNoeud] for x in tableau_degree_centrality])
        sns.tsplot(tab[i], color = "blue")
        i+=1
    if 'c' in liste:
        tab.append([x[numNoeud] for x in tableau_closeness_centrality])
        sns.tsplot(tab[i], color = "red")
        i+=1
    if 'p' in liste:
        tab.append([x[numNoeud] for x in tableau_pagerank])
        sns.tsplot(tab[i], color = "black")
        i+=1
    if 'b' in liste:
        tab.append([x[numNoeud] for x in tableau_betweeness])
        sns.tsplot(tab[i], color = "green")
        i+=1


def recherche_nom() :
    continu = "o"
    while continu == "o" :
        nomNoeud = str(input("Entrez le nom du personnage : "))
        numNoeud = dicoNomToNum[nomNoeud]
        
        type_centralite_voulu(numNoeud)
        
        """sns.tsplot(tab[0])
        plt.savefig("images/n93.jpg")
        plt.show()"""
        print("")
        print(" Bleu = degree   |   Rouge = Closeness   |   Noir = Pagerank   |   Vert = Betweeness")
        plt.show()
        continu = str(input("Entrez o pour rentrez un perso à nouveau : "))
        



""" On crée un dictionnaire qui associe les noms des persos à leur numéro de noeud """
G1=nx.read_graphml("data\GoT_S05E09_1039.graphml")
dicoNumToNom = nx.get_node_attributes(G1,"label")
dicoNomToNum = {dicoNumToNom[cle]:cle for cle in dicoNumToNom}
    
    
plage = int(input("Nombre de scènes : "))
if plage > 1039 :
    plage = 1039
liste_graph = []
for element in os.listdir('data')[:plage]:
    liste_graph.append(nx.read_graphml('data\\' + str(element)))
        
tableau_closeness_centrality = []
tableau_degree_centrality = []
tableau_pagerank = []
tableau_betweeness = []
for l in liste_graph :
    #l.remove_nodes_from(nx.isolates(l))  ==> Pour enlever les isolates mais on doit les garder pour avoir de bonnes valeurs sur la courbe
    """nx.draw_networkx(l,pos=nx.spring_layout(l))  == >  Affichage du graphe de la case liste_graph(l)"""
    tableau_degree_centrality.append(nx.degree_centrality(l))  # une façon de lire la centralité
    tableau_closeness_centrality.append(nx.closeness_centrality(l))
    tableau_pagerank.append(nx.pagerank(l))
    tableau_betweeness.append(nx.betweenness_centrality(l))
        
numNoeud = ""    
recherche_nom()
 
 
""" 
Idée amélioration : 
 
- Chercher les 3 persos avec la plus grosse centralité
- Fusionner des graphes pour avoir une centralité plus importante
- Changer de façon pour la centralité (autre que degree_centrality())
- Pouvoir choisir le type de centralité
- Pouvoir lire plusieurs persos sans fermer le code
 """