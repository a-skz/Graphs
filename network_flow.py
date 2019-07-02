from graph_list import DirectedListGraph
from graph_matrix import DirectedMatrixGraph
from graph_utilities import GraphSearch

class NetworkFlow():

    def __init__(self, G):
        self.n = [{'v':i, 'a':{j:[0, G.get_weight(i,j)] for j in G.get_adjacent(i)}} for i in range(G.get_vertices())]


    def get_residual(self, i, j):
        return self.n[i]['a'][j][1]-self.n[i]['a'][j][0]

    def maximum_flow(self, s, t):
        max_flow = 0
        while(True):
            aux = DirectedListGraph(len(self.n))
            for v in self.n:
                for e in v['a'].keys():
                    if v['a'][e][0]!=v['a'][e][1]: aux.add_edge(v['v'], e)

            bfs = GraphSearch.run_bfs(aux, s)
            path = [(bfs[t]['pi'], t)]
            while True:
                if path[-1][0]==None:
                    break
                if bfs[path[-1][0]]['pi']==None:
                    break
                path.append((bfs[path[-1][0]]['pi'], path[-1][0]))            
            path.reverse()

            if (path[0][0]!=s):
                return max_flow

            min_cap = min([self.get_residual(i,j) for i,j in path])
            
            for i,j in path:
                self.n[i]['a'][j][0] += min_cap
            
            max_flow += min_cap