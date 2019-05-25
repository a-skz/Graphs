from grafos import Graph

print("\nDirected List Graph")
g = Graph.generate(9, rep='list', dirc=True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(5,1)
g.add_edge(5,2)
g.add_edge(5,3)
g.add_edge(6,1)
g.add_edge(6,4)
g.add_edge(6,7)
g.add_edge(7,6)
g.add_edge(8,7)
g.to_string()
print('Number of vertices: ', g.get_vertices())
print('Number of edges: ', g.get_edges())
print('Maximum order: ', g.get_max_order())
print('Number of loops: ', g.get_loops())
print("-- DFS Search --")
for x in Graph.dfs_search(g): print(x)
print("-- BFS Search --")
for x in Graph.bfs_search(g): print(x)

print("\nUndirected List Graph")
g = Graph.generate(5, rep='list')
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.to_string()
print("--")
print('Adjacents of 1: ', g.get_adjacent(1))
print('Number of edges: ', g.get_edges())
print('Maximum order: ', g.get_max_order())
print('Is eulerian? ', g.is_eulerian())
print('Has open eulerian path? ', g.has_open_eule_path())
print("-- DFS Search --")
for x in Graph.dfs_search(g): print(x)
print("-- BFS Search --")
for x in Graph.bfs_search(g): print(x)

print("\nDirected Matrix Graph")
g = Graph.generate(9, rep='matrix', dirc=True)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,4)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(4,5)
g.add_edge(5,1)
g.add_edge(5,2)
g.add_edge(5,3)
g.add_edge(6,1)
g.add_edge(6,4)
g.add_edge(6,7)
g.add_edge(7,6)
g.add_edge(8,7)
g.to_string()
print('Number of vertices: ', g.get_vertices())
print('Number of edges: ', g.get_edges())
print('Maximum order: ', g.get_max_order())
print('Number of loops: ', g.get_loops())
print("--")
for x in Graph.dfs_search(g): print(x)
print("--")
for x in Graph.bfs_search(g): print(x)

print("Undirected Matrix Graph")
g = Graph.generate(5, rep='matrix')
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.to_string()
print("--")
print('Adjacents of 1: ', g.get_adjacent(1))
print('Number of edges: ', g.get_edges())
print('Maximum order: ', g.get_max_order())
print('Is eulerian? ', g.is_eulerian())
print('Has open eulerian path? ', g.has_open_eule_path())
print("--")
for x in Graph.dfs_search(g): print(x)
print("--")
for x in Graph.bfs_search(g): print(x)