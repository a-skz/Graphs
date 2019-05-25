import random
from graph import GraphFactory, GraphSearch, UndirectedMatrixGraph

def test_graph(v, *, rep, dirc, edges):
    print('Begin test')
    G = GraphFactory.generate_graph(v, rep=rep, dirc=dirc)
    test_general_graph(G, edges)
    
    if dirc:
        test_directed_graph(G)
    else:
        test_undirected_graph(G)
    
    test_search_graph(G)
    print('End test\n\n')

def test_general_graph(G, edges):

    for v,w in edges:
        G.add_edge(v, w)
    G.to_string()
    v = G.get_vertices()
    print('Number of vertices: ', v)
    i = random.randint(0, v-1)
    print('Adjacents of vertice ', i, ':', G.get_adjacent(i))
    l = G.get_loops()
    print('Number of loops: ', l)

def test_directed_graph(G):

    v = G.get_vertices()
    i = random.randint(0, v-1)
    e = G.get_edges()
    print('Number of edges: ', e)
    print('Order of vertice ', i, ':', G.get_order(i))
    max_o = G.get_max_order()
    print('Maximum order: ', max_o)

    if isinstance(G, UndirectedMatrixGraph):
        c = G.get_transitive_closure()
        print('Transitive Closure: ')
        for row in c: print(row)

def test_undirected_graph(G):

    v = G.get_vertices()
    i = random.randint(0, v-1)
    e = G.get_edges()
    print('Number of edges: ', e)
    print('Order of vertice ', i, ':', G.get_order(i))
    max_o = G.get_max_order()
    print('Maximum order: ', max_o())
    is_eule = G.is_eulerian()
    print('Is eulerian? ', is_eule)
    has_open_eule = G.has_open_eule_path()
    print('Has open eulerian path? ', has_open_eule)


def test_search_graph(G, s=0):
    print("-- DFS Search --")
    for x in GraphSearch.get_dfs_search(G): print(x)
    print("-- BFS Search --")
    for x in GraphSearch.get_bfs_search(G, s): print(x)