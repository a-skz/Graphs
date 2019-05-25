from graphs import Graph

def directed_graph(rep, vertices, edges=[]):
    print("\nDirected ", rep, "Graph")
    g = Graph.generate(vertices, rep=rep, dirc=True)
    for v,w in edges:
        g.add_edge(v, w)
    g.to_string()
    print('Number of vertices: ', g.get_vertices())
    print('Number of edges: ', g.get_edges())
    print('Adjacents of vertice 1: ', g.get_adjacent(1))
    print('Order of vertice 1', g.get_order(1))
    print('Maximum order: ', g.get_max_order())
    print('Number of loops: ', g.get_loops())
    print("-- DFS Search --")
    for x in Graph.dfs_search(g): print(x)
    print("-- BFS Search --")
    for x in Graph.bfs_search(g): print(x)
    if rep=='matrix':
        print("-- Transitive Closure --")
        a = g.transitive_closure()
        for row in a: print(row)

def undirected_graph(rep, verticies, edges=[]):
    print("\nUndirected ", rep, "Graph")
    g = Graph.generate(verticies, rep=rep, dirc=False)
    for v,w in edges:
        g.add_edge(v, w)
    g.to_string()
    print('Number of vertices: ', g.get_vertices())
    print('Number of edges: ', g.get_edges())
    print('Adjacents of vertice 1: ', g.get_adjacent(1))
    print('Order of vertice 1', g.get_order(1))
    print('Maximum order: ', g.get_max_order())
    print('Number of loops: ', g.get_loops())
    print('Is eulerian? ', g.is_eulerian())
    print('Has open eulerian path? ', g.has_open_eule_path())
    print("-- DFS Search --")
    for x in Graph.dfs_search(g): print(x)
    print("-- BFS Search --")
    for x in Graph.bfs_search(g): print(x)