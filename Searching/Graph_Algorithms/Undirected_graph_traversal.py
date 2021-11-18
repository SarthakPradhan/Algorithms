edges = [['i','j'],['k','i'],['m','k'],['k','l'],['o','n']]

def Undir_path_search(node,goal):
    graph = makeGraph(edges)
    visited = set()
    print(hasPath_DF(graph,node,goal,visited))

def makeGraph(edges):
    graph = {}
    for [e1,e2] in edges:
        if not(e1 in graph): graph[e1]=[]
        if not(e2 in graph): graph[e2]=[]

        graph[e1].append(e2)
        graph[e2].append(e1)

    print('The adjacency list is',graph)
    return graph

def hasPath_DF(graph,node,goal,visited):
    if node == goal: return True
    if node in visited: return False
    visited.add(node)
    neighbours = graph[node]
    for n in neighbours:
        if hasPath_DF(graph,n,goal,visited):
            return True

    return False

Undir_path_search('j','z')