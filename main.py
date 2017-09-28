import networkx as nx

#essai de graph

G=nx.read_graphml("GoT_dyn_ts40\GoT_S01E01_000.graphml")
print("nombre de  noeuds")
print(G.number_of_nodes())
print("nombre de bords")
print(G.number_of_edges())

print(G.neighbors("n23"))
"""print ("yolooopo")
print(len(nx.isolates(G)))"""

