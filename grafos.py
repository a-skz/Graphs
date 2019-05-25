class Graph(object):
    
    @classmethod
    def generate(cls, v, *, rep = 'list', dirc = False):
        if dirc:
            if rep == 'list':
                return DirectedListGraph(v)
            elif rep == 'matrix':
                return DirectedMatrixGraph(v)
            else:
                raise ValueError('Representation not found.')
        
        else:
            if rep == 'list':
                return UndirectedListGraph(v)
            elif rep == 'matrix':
                return UndirectedMatrixGraph(v)
            else:
                raise ValueError('Representation not found.')
                
    @staticmethod
    def dfs_search(G):
        g = [{'v':i, 'a':G.get_adjacent(i), 'c':'b', 'd':0,'f':0,'pi':None, 'id':None} for i in range(G.get_vertices())]
        time = 0
        group = 0
        for v in g:
            if v['c'] == 'b':
                time = Graph.dfs_visit(v, g, time, group)
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
                time = Graph.dfs_visit(g[a], g, time, group)
        v['c'] = 'p'
        time +=1
        v['f'] = time
        return time

    @staticmethod
    def bfs_search(G):
        g = [{'v':i, 'a':G.get_adjacent(i), 'c':'b', 'd':0,'pi':None} for i in range(G.get_vertices())]
        g[0]['c'] = 'c'
        Q = [g[0]['v']]
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

class DirectedListGraph(object):
    
    def __init__(self, v):
        self.g = {i:{'a':[], 'in_o':0, 'out_o':0, 'w':0} for i in range(v)}
        
    def get_vertices(self):
        return len(self.g.keys())
    
    def get_edges(self):
        A = [len(v['a']) for v in self.g.values()]
        return sum(A)
        
    def add_edge(self, v, w):
        self.g[v]['a'].append(w)
        self.g[v]['out_o'] += 1
        self.g[w]['in_o'] += 1
            
    def get_adjacent(self, v):
        return self.g[v]['a']
    
    def get_order(self, v):
        return (self.g[v]['in_o'], self.g[v]['out_o'])
    
    def get_max_order(self):
        in_o = sorted(self.g.values(), key=lambda x: x['in_o'])
        out_o = sorted(self.g.values(), key=lambda x: x['out_o'])
        return (in_o[-1]['in_o'], out_o[-1]['out_o'])
    
    def get_loops(self):
        loops = [1 for v in self.g.keys() if v in self.g[v]['a']]
        return sum(loops)
    
    def to_string(self):
        for vertice, attributes in self.g.items():
            print(vertice, ':', attributes)

class UndirectedListGraph(DirectedListGraph):
    
    def __init__(self, v):
        super().__init__(v)
        self.g = {i:{'a':[], 'o':0, 'w':0} for i in range(v)}
    
    def get_edges(self):
        A = [len(v['a']) for v in self.g.values()]
        return sum(A)/2
    
    def add_edge(self, v, w):
        self.g[v]['a'].append(w)
        self.g[v]['o'] += 1
        self.g[w]['a'].append(v)
        self.g[w]['o'] += 1
    
    def get_order(self,v):
        return self.g[v]['o']
    
    def get_max_order(self):
        g = sorted(self.g.values(), key=lambda x: x['o'])
        return g[-1]['o']
    
    def is_eulerian(self):
        for v in self.g.values():
            if (v['o']%2 != 0): return False
        return True
    
    def has_open_eule_path(self):
        odd = [1 for v in self.g.values() if v['o']%2 != 0]
        if len(odd) > 2:
            return False
        return True

class DirectedMatrixGraph(object):
    
    def __init__(self, v):
        self.g = [[0 for i in range(v)] for i in range(v)]
        self.order = [{'in_o':0, 'out_o':0} for i in range(v)]
        
    def get_vertices(self):
        return len(self.g)
    
    def get_edges(self):
        A = [sum(row) for row in self.g]
        return sum(A)

    def add_edge(self, v, w):
        self.g[v][w] = 1
        self.order[v]['in_o'] += 1
        self.order[w]['out_o'] += 1
    
    def get_adjacent(self, v):
        return [adjacent[0] for adjacent in enumerate(self.g[v]) if adjacent[1] == 1]
    
    def get_order(self, v):
        return self.order[v]
        
    def get_max_order(self):
        in_o = [order['in_o'] for order in self.order]
        out_o = [order['out_o'] for order in self.order]
        return (max(in_o), max(out_o))
    
    def get_loops(self):
        loops = [1 for l in range(len(self.g)) if self.g[l][l] == 1]
        return sum(loops)
    
    def to_string(self):
        head = '   '
        for i in range(len(self.g)):
            head += str(i) + '  '
        print(head)
        for i in range(len(self.g)):
            print(i, self.g[i])

class UndirectedMatrixGraph(DirectedMatrixGraph):
    
    def __init__(self, v):
        super().__init__(v)
        self.order = [0 for i in range(v)]
        
    def get_vertices(self):
        return len(self.g)
    
    def get_edges(self):
        A = [sum(row) for row in self.g]
        return sum(A)/2

    def add_edge(self, v, w):
        self.g[v][w] = 1
        self.g[w][v] = 1
        self.order[v] += 1
        self.order[w] += 1
    
    def get_order(self, v):
        return self.order[v]
        
    def get_max_order(self):
        return max(self.order)
            
    def is_eulerian(self):
        for order in self.order:
            if (order%2 != 0): return False
        return True

    def has_open_eule_path(self):
        odd = 0
        for order in self.order:
            if (order%2 != 0): odd += 1
            if (odd > 2): return False
        if (odd != 2): return False
        return True
