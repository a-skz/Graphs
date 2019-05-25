import test

representations = ['list', 'matrix']

vertices = 9
edges = [(0,1), (1,2), (1,4), (2,0), (2,3), (4,5), (5,1),
         (5,2), (5,3), (6,1), (6,4), (6,7), (7,6), (8,7)]
for representation in representations:
    test.directed_graph(representation, vertices, edges)

vertices = 5
edges = [(0,1), (0,2), (0,3), (1,3), (2,3), (3,4)]
for representation in representations:
    test.undirected_graph(representation, vertices, edges)

representations = ['matrix']

vertices = 4
edges = [(0,1), (1,2), (2,3)]
for representation in representations:
    test.directed_graph(representation, vertices, edges)