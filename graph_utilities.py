class GraphSearch(object):

    @staticmethod
    def run_dfs(G, s=None):
        if not s: s = [i for i in range(G.get_vertices())]
        g = [{'v':i, 'a':G.get_adjacent(i), 'c':'b', 'd':0, 'f':0, 'pi':None, 'id':None} for i in range(G.get_vertices())]
        group = 0
        time = 0
        for v in g:
            if v['c'] == 'b':
                time = GraphSearch.dfs_visit(v, g, time, group)
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
    def run_bfs(G, s):
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

class ShortestPath(object):

    @staticmethod
    def init_single_source(G, s):
        g = [{'v':i, 'd':999, 'pi':None} for i in range(G.get_vertices())]
        g[s]['d'] = 0
        return g 

    @staticmethod
    def relax(u, v, w):
        if (not v['d']) or (v['d']>u['d']+w):
            v['d'] = u['d'] + w
            v['pi'] = u['v']

    @staticmethod
    def dijkstra_algorithm(G, s):
        g = ShortestPath.init_single_source(G, s)
        S = []
        Q = [i for i in range(G.get_vertices())]
        while(len(Q)>0):
            Q = sorted(Q, key=lambda x: g[x]['d'])
            u = Q.pop(0)
            S.append(g[u])
            for v in G.get_adjacent(u):
                if v!=s: ShortestPath.relax(g[u], g[v], G.get_weight(u,v))
        return g