import networkx as nx
import matplotlib.pyplot as plt
#from networkx.drawing.nx_agraph import graphviz_layout
#essai de graph

G1=nx.read_graphml("data\GoT_S05E09_1039.graphml")
print("nombre de  noeuds")
print(G1.number_of_nodes())
print("nombre de bords")
print(G1.number_of_edges())

print(G1.neighbors("n23"))

G1.remove_nodes_from(nx.isolates(G1))

nx.draw_networkx_labels(G1,pos=nx.spring_layout(G1))
plt.draw()


"""attributes = {
"with_labels" : True,
}
plot = plt.subplots()
pos = graphviz_layout(G1)
nx.draw_networkx(G1, pos, **attributes)
"""


"""
G2=nx.read_graphml("data\GoT_S01E01_001.graphml")
print("nombre de  noeuds")
print(G2.number_of_nodes())
print("nombre de bords")
print(G2.number_of_edges())

print(G2.neighbors("n23"))
print ("yolooopo")
print(len(nx.isolates(G)))
G2.remove_nodes_from(nx.isolates(G2))
nx.draw(G2,pos=nx.spring_layout(G2))

"""
