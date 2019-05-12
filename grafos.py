class Grafo(object):
    
    @staticmethod
    def generate(v, *, rep = 'lista', dirc = False):
        if dirc:
            if rep == 'lista':
                return ListaD(v)
            elif rep == 'matriz':
                return MatrizD(v)
            else:
                raise ValueError('Representation not found.')
        
        else:
            if rep == 'lista':
                return ListaND(v)
            elif rep == 'matriz':
                return MatrizND(v)
            else:
                raise ValueError('Representation not found.')
                
    @staticmethod
    def busca_dfs(G):
        g = [{'v':i, 'a':G.get_adj(i), 'c':'b', 'd':0,'f':0,'pi':None, 'id':None} for i in range(G.get_V())]
        tempo = 0
        comp = 0
        for v in g:
            if v['c'] == 'b':
                tempo = Grafo.visita_dfs(v, g, tempo, comp)
                comp += 1
        return g

    @staticmethod
    def visita_dfs(v, g, tempo, comp):
        v['c'] = 'c'
        tempo += 1
        v['d'] = tempo
        v['id'] = comp
        for a in v['a']:
            if g[a]['c'] == 'b':
                g[a]['pi'] = v['v']
                tempo = Grafo.visita_dfs(g[a], g, tempo, comp)
        v['c'] = 'p'
        tempo +=1
        v['f'] = tempo
        return tempo

    @staticmethod
    def busca_bfs(G):
        g = [{'v':i, 'a':G.get_adj(i), 'c':'b', 'd':0,'pi':None} for i in range(G.get_V())]
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

class ListaD(object):
    
    def __init__(self, v):
        self.g = [{'v':i, 'a':[], 'g_e':0, 'g_s':0} for i in range(v)]
        
    def get_V(self):
        return len(self.g)
    
    def get_A(self):
        A = [len(v['a']) for v in self.g]
        return sum(A)
        
    def add_A(self, v, w):
        self.g[v]['a'].append(w)
        self.g[v]['g_s'] += 1
        self.g[w]['g_e'] += 1
            
    def get_adj(self, v):
        return self.g[v]['a']
    
    def get_grau(self,v):
        return (self.g[v]['g_e'], self.g[v]['g_s'])
    
    def get_max_grau(self):
        g_e = sorted(self.g, key=lambda x: x['g_e'])
        g_s = sorted(self.g, key=lambda x: x['g_s'])
        return (g_e[-1]['g_e'], g_s[-1]['g_s'])
    
    def get_lacos(self):
        lacos = [1 for v in self.g if v['v'] in v['a']]
        return sum(lacos)
    
    def to_string(self):
        for v in self.g:
            print(v)

class ListaND(ListaD):
    
    def __init__(self, v):
        super().__init__(v)
        self.g = [{'v':i, 'a':[], 'g':0} for i in range(v)]
    
    def get_A(self):
        A = [len(v['a']) for v in self.g]
        return sum(A)/2
    
    def add_A(self, v, w):
        self.g[v]['a'].append(w)
        self.g[v]['g'] += 1
        self.g[w]['a'].append(v)
        self.g[w]['g'] += 1
    
    def get_grau(self,v):
        return self.g[v]['g']
    
    def get_max_grau(self):
        g = sorted(self.g, key=lambda x: x['g'])
        return g[-1]['g']
    
    def is_eule(self):
        for v in self.g:
            if (v['g']%2 != 0): return False
        return True
    
    def has_eule_aberto(self):
        impar = [1 for v in self.g if v['g']%2 != 0]
        if len(impar) > 2:
            return False
        return True

class MatrizD(object):
    
    def __init__(self, v):
        self.g = [[0 for i in range(v)] for i in range(v)]
        self.grau = [{'g_e':0, 'g_s':0} for i in range(v)]
        
    def get_V(self):
        return len(self.g)
    
    def get_A(self):
        A = [sum(linha) for linha in self.g]
        return sum(A)

    def add_A(self, v, w):
        self.g[v][w] = 1
        self.grau[v]['g_e'] += 1
        self.grau[w]['g_s'] += 1
    
    def get_adj(self, v):
        return [adj[0] for adj in enumerate(self.g[v]) if adj[1] == 1]
    
    def get_grau(self, v):
        return self.grau[v]
        
    def get_max_grau(self):
        g_e = [grau['g_e'] for grau in self.grau]
        g_s = [grau['g_s'] for grau in self.grau]
        return (max(g_e), max(g_s))
    
    def get_lacos(self):
        lacos = [1 for l in range(len(self.g)) if self.g[l][l] == 1]
        return sum(lacos)
    
    def to_string(self):
        head = '   '
        for i in range(len(self.g)):
            head += str(i) + '  '
        print(head)
        for i in range(len(self.g)):
            print(i, self.g[i])

class MatrizND(MatrizD):
    
    def __init__(self, v):
        super().__init__(v)
        self.grau = [0 for i in range(v)]
        
    def get_V(self):
        return len(self.g)
    
    def get_A(self):
        A = [sum(linha) for linha in self.g]
        return sum([sum(row) for row in self.g])/2

    def add_A(self, v, w):
        self.g[v][w] = 1
        self.g[w][v] = 1
        self.grau[v] += 1
        self.grau[w] += 1
    
    def get_grau(self, v):
        return self.grau[v]
        
    def get_max_grau(self):
        return max(self.grau)
            
    def is_eule(self):
        for grau in self.grau:
            if (grau%2 != 0): return False
        return True
    
    def has_eule_aberto(self):
        impar = 0
        for grau in self.grau:
            if (grau%2 != 0): impar += 1
            if (impar > 2): return False
        if (impar != 2): return False
        return True
