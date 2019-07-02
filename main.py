from graph_list import DirectedListGraph
from graph_matrix import DirectedMatrixGraph
from graph_utilities import GraphSearch
from network_flow import NetworkFlow

v=6
e = [(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]
# e = [(0,1,10),(0,2,10),(1,2,2),(1,3,4),(1,4,8),(2,4,9),(3,5,10),(4,3,6),(4,5,10)]
# g = DirectedListGraph(v)
g = DirectedMatrixGraph(v)
for a,b,weight in e: g.add_edge(a,b,weight)

n = NetworkFlow(g)
max_flow = n.maximum_flow(0,5)
print(max_flow)
