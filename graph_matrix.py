from graph_utilities import GraphSearch

class MatrixGraph(object):
    def __init__(self, v):
        self.g = [[0 for i in range(v)] for i in range(v)]
        self.w = [[0 for i in range(v)] for i in range(v)]
    
    def get_vertices(self):
        return len(self.g)

    def get_edges(self):
        A = [sum(row) for row in self.g]
        return sum(A)

    def add_edge(self, v, u, w):
        self.g[v][u] = 1
        self.w[v][u] = w

    def get_adjacent(self, v):
        return [a[0] for a in enumerate(self.g[v]) if a[1] == 1]
    
    def get_weight(self, v, u):
        return self.w[v][u]

    def get_loops(self):
        loops = [1 for i in range(len(self.g)) if self.g[i][i] == 1]
        return sum(loops)
    
    def to_string(self):
        head = '   '
        for i in range(len(self.g)):
            head += str(i) + '  '
        print(head)
        for i in range(len(self.g)):
            print(i, self.g[i])


class DirectedMatrixGraph(MatrixGraph):
    def __init__(self, v):
        super().__init__(v)
        self.o = [{'in_o':0, 'out_o':0} for i in range(v)]

    def add_edge(self, v, u, w=0):
        super().add_edge(v, u, w)
        self.o[v]['out_o'] += 1
        self.o[u]['in_o'] += 1
    
    def get_order(self, v):
        in_o = self.o[v]['in_o']
        out_o = self.o[v]['out_o']
        return (in_o, out_o)

    def get_max_order(self):
        in_o = [o['in_o'] for o in self.o]
        out_o = [o['out_o'] for o in self.o]
        return (max(in_o), max(out_o))

    def get_transitive_closure(self):
        a = [row for row in self.g]
        n = len(a)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if (a[i][j]==0):
                        if (a[i][k]==1) and (a[k][j]==1):
                            a[i][j] = 1
        return a

    def get_topological_order(self):
        s = [i for i in range(self.get_vertices())]
        s = sorted(s, key=lambda x: self.get_order(x)[0])
        t = GraphSearch.get_dfs_search(self, s)
        t = sorted(t, key=lambda x: x['f'], reverse=True)
        t = [{'v':x['v'], 'a':x['a']} for x in t]
        return t

    def get_transpose_graph(self):
        gt = DirectedMatrixGraph(self.get_vertices())
        for v in range(self.get_vertices()):
            for w in self.get_adjacent(v):
                gt.add_edge(w, v)
        return gt

    def get_strongly_connected_comps(self):
        dfs = GraphSearch.get_dfs_search(self)
        dfs = sorted(dfs, key=lambda x: x['f'], reverse=True)
        gt = self.get_transpose_graph()
        s = [i for i in range(gt.get_vertices())]
        s = sorted(s, key=lambda x: dfs[x]['f'], reverse=True)
        dfs = GraphSearch.get_dfs_search(gt, s)
        dfs = sorted(dfs, key=lambda x: x['id'])
        return dfs

class UndirectedMatrixGraph(MatrixGraph):
    def __init__(self, v):
        super().__init__(v)
        self.o = [0 for i in range(v)]

    def get_edges(self):
        A = super().get_edges()
        return A/2

    def add_edge(self, v, u, w=0):
        super().add_edge(v, u, w)
        self.o[v] += 1
        super().add_edge(w, u, w)
        self.o[u] += 1

    def get_order(self, v):
        return self.o[v]

    def get_max_order(self):
        return max(self.o)

    def is_eulerian(self):
        for o in self.o:
            if (o%2 != 0): return False
        return True

    def has_open_eule_path(self):
        odd = 0
        for o in self.o:
            if (o%2 != 0): odd += 1
            if (odd > 2): return False
        if (odd != 2): return False
        return True