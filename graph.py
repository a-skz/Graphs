class ListGraph(object):
    def __init__(self, v):
        self.g = {i:{'a':[]} for i in range(v)}

    def get_vertices(self):
        return len(self.g.keys())

    def get_adjacent(self, v):
        return self.g[v]['a']

    def get_edges(self):
        A = [len(self.get_adjacent(v)) for v in range(self.get_vertices())]
        return sum(A)

    def add_edge(self, v, w):
        self.g[v]['a'].append(w)

    def get_loops(self):
        loops = [1 for v in range(self.get_vertices()) if v in self.get_adjacent(v)]
        return sum(loops)

    def to_string(self):
        for vertice, attributes in self.g.items():
            print(vertice, ':', attributes)
    

class DirectedListGraph(ListGraph):
    def __init__(self, v):
        super().__init__(v)
        for v in range(self.get_vertices()):
            self.g[v]['in_o'] = 0
            self.g[v]['out_o'] = 0

    def add_edge(self, v, w):
        super().add_edge(v, w)
        self.g[v]['out_o'] += 1
        self.g[w]['in_o'] += 1

    def get_order(self, v):
        return (self.g[v]['in_o'], self.g[v]['out_o'])

    def get_max_order(self):
        o = [self.get_order(v) for v in range(self.get_vertices())]
        o = list(zip(*o))
        in_o = sorted(o[0])
        out_o = sorted(o[1])
        return (in_o[-1], out_o[-1])
    
    def get_topological_order(self):
        t = GraphSearch.get_dfs_search(self)
        t = sorted(t, key=lambda x: x['f'], reverse=True)
        t = [{'v':x['v'], 'a':x['a']} for x in t]
        return t


class UndirectedListGraph(ListGraph):
    def __init__(self, v):
        super().__init__(v)
        for v in range(self.get_vertices()):
            self.g[v]['o'] = 0

    def get_edges(self):
        A = super().get_edges()
        return A/2

    def add_edge(self, v, w):
        super().add_edge(v, w)
        self.g[v]['o'] += 1
        super().add_edge(w, v)
        self.g[v]['o'] += 1

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


class MatrixGraph(object):
    def __init__(self, v):
        self.g = [[0 for i in range(v)] for i in range(v)]
    
    def get_vertices(self):
        return len(self.g)

    def get_edges(self):
        A = [sum(row) for row in self.g]
        return sum(A)

    def add_edge(self, v, w):
        self.g[v][w] = 1

    def get_adjacent(self, v):
        return [a[0] for a in enumerate(self.g[v]) if a[1] == 1]
    
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

    def add_edge(self, v, w):
        super().add_edge(v, w)
        self.o[v]['out_o'] += 1
        self.o[w]['in_o'] += 1
    
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
        t = GraphSearch.get_dfs_search(self)
        t = sorted(t, key=lambda x: x['f'], reverse=True)
        t = [{'v':x['v'], 'a':x['a']} for x in t]
        return t


class UndirectedMatrixGraph(MatrixGraph):
    def __init__(self, v):
        super().__init__(v)
        self.o = [0 for i in range(v)]

    def get_edges(self):
        A = super().get_edges()
        return A/2

    def add_edge(self, v, w):
        super().add_edge(v, w)
        self.o[v] += 1
        super().add_edge(w, v)
        self.o[w] += 1

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

class GraphSearch(object):

    @staticmethod
    def get_dfs_search(G):
        s = [i for i in range(G.get_vertices())]
        if isinstance(G.get_order(0), tuple):
            s = sorted(s, key=lambda x: G.get_order(x)[0])
        else:
            s = sorted(s, key=lambda x: G.get_order(x))
        g = [{'v':i, 'a':G.get_adjacent(i), 'c':'b', 'd':0, 'f':0, 'pi':None, 'id':None} for i in s]
        group = 0
        for v in g:
            if v['c'] == 'b':
                GraphSearch.dfs_visit(v, g, 0, group)
                group += 1
        return g

    @staticmethod
    def dfs_visit(v, g, time, group):
        v['c'] = 'c'
        time += 1
        v['d'] = time
        v['id'] = group
        for a in v['a']:
            if g[a]['c'] == 'b':
                g[a]['pi'] = v['v']
                time = GraphSearch.dfs_visit(g[a], g, time, group)
        v['c'] = 'p'
        time +=1
        v['f'] = time
        return time

    @staticmethod
    def get_bfs_search(G, s):
        g = [{'v':i, 'a':G.get_adjacent(i), 'c':'b', 'd':0,'pi':None} for i in range(G.get_vertices())]
        g[s]['c'] = 'c'
        Q = [g[s]['v']]
        while (len(Q) != 0):
            u = Q.pop(0)
            for v in g[u]['a']:
                if g[v]['c'] == 'b':
                    g[v]['c'] = 'c'
                    g[v]['d'] = g[u]['d'] + 1
                    g[v]['pi'] = g[u]['v']
                    Q.append(v)
            g[u]['c'] = 'p'
        return g

class GraphFactory(object):

    @staticmethod
    def generate_graph(v, *, rep='list', dirc=True):
        if rep=='list':
            if dirc: return DirectedListGraph(v)
            else: return UndirectedListGraph(v)
        elif rep=='matrix':
            if dirc: return DirectedMatrixGraph(v)
            else: return UndirectedMatrixGraph(v)
        else:
            raise ValueError('Representation not found.')       
