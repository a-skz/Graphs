from graph_utilities import GraphSearch
from graph_matrix import DirectedMatrixGraph

class ListGraph(object):
    def __init__(self, v):
        self.g = [{'v':i, 'a':[]} for i in range(v)]

    def get_vertices(self):
        return len(self.g)

    def get_adjacent(self, v):
        a = [i[0] for i in self.g[v]['a']]
        return a

    def get_weight(self, v, u):
        for i,a in enumerate(self.get_adjacent(v)):
            if a==u: return self.g[v]['a'][i][1]
        return None

    def get_edges(self):
        A = [len(self.get_adjacent(v)) for v in range(self.get_vertices())]
        return sum(A)

    def add_edge(self, v, u, p):
        self.g[v]['a'].append((u,p))

    def get_loops(self):
        loops = [1 for v in range(self.get_vertices()) if v in self.get_adjacent(v)]
        return sum(loops)

    def to_string(self):
        for v in self.g: 
            print(v)
    

class DirectedListGraph(ListGraph):
    def __init__(self, v):
        super().__init__(v)
        for v in range(self.get_vertices()):
            self.g[v]['in_o'] = 0
            self.g[v]['out_o'] = 0

    def add_edge(self, v, u, w=0):
        super().add_edge(v, u, w)
        self.g[v]['out_o'] += 1
        self.g[u]['in_o'] += 1

    def get_order(self, v):
        return (self.g[v]['in_o'], self.g[v]['out_o'])

    def get_max_order(self):
        o = [self.get_order(v) for v in range(self.get_vertices())]
        o = list(zip(*o))
        in_o = sorted(o[0])
        out_o = sorted(o[1])
        return (in_o[-1], out_o[-1])
    
    def get_transitive_closure(self):
        m = DirectedMatrixGraph(self.get_vertices())
        for v in range(self.get_vertices()):
            for u in self.get_adjacent(v):
                m.add_edge(v, u, self.get_weight(v,u))
        tc = m.get_transitive_closure()
        return tc

    def get_topological_order(self):
        s = [i for i in range(self.get_vertices())]
        s = sorted(s, key=lambda x: self.get_order(x)[0])
        t = GraphSearch.get_dfs_search(self, s)
        t = sorted(t, key=lambda x: x['f'], reverse=True)
        t = [{'v':x['v'], 'a':x['a']} for x in t]
        return t

    def get_transpose_graph(self):
        g = DirectedListGraph(self.get_vertices())
        for v in range(self.get_vertices()):
            for w in self.get_adjacent(v):
                g.add_edge(w, v)
        return g

    def get_strongly_connected_comps(self):
        dfs = GraphSearch.get_dfs_search(self)
        dfs = sorted(dfs, key=lambda x: x['f'], reverse=True)
        gt = self.get_transpose_graph()
        s = [i for i in range(gt.get_vertices())]
        s = sorted(s, key=lambda x: dfs[x]['f'], reverse=True)
        dfs = GraphSearch.get_dfs_search(gt, s)
        dfs = sorted(dfs, key=lambda x: x['id'])
        return dfs

class UndirectedListGraph(ListGraph):
    def __init__(self, v):
        super().__init__(v)
        for v in range(self.get_vertices()):
            self.g[v]['o'] = 0

    def get_edges(self):
        A = super().get_edges()
        return A/2

    def add_edge(self, v, u, w=0):
        super().add_edge(v, u, w)
        self.g[v]['o'] += 1
        super().add_edge(u, v, w)
        self.g[u]['o'] += 1

    def get_order(self, v):
        return self.g[v]['o']

    def get_max_order(self):
        o = [self.get_order(v) for v in range(self.get_vertices())]
        return max(o)

    def is_eulerian(self):
        for v in range(self.get_vertices()):
            if self.get_order(v)%2!=0:
                return False
        return True
    
    def has_open_eule_path(self):
        odd = 0
        for v in range(self.get_vertices()):
            if self.get_order(v)%2!=0:
                odd+=1
            if odd > 2:
                return False
        if (odd!=2):
            return False
        return True