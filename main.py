import test

edges = [(0,1), (1,2), (1,4), (2,0), (2,3), (4,5), (5,1),
         (5,2), (5,3), (6,1), (6,4), (6,7), (7,6), (8,7)]
for rep in ['list', 'matrix']:
    test.test_graph(9, rep=rep, dirc=True, edges=edges)

edges = [(0,1),(0,2),(1,2),(1,3),(2,3),(2,4)]
for rep in ['list', 'matrix']:
    test.test_graph(5, rep=rep, dirc=True, edges=edges)

edges = [(0,1), (1,2), (2,3)]
for rep in ['matrix']:
    test.test_graph(4, rep=rep, dirc=True, edges=edges)

edges = [(0,1), (0,2), (0,3), (1,3), (2,3), (3,4)]
for rep in ['list', 'matrix']:
    test.test_graph(5, rep=rep, dirc=False, edges=edges)