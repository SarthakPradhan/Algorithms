edges = [['w','x'],['x','y'],['z','y'],['z','v'],['w','v']]


def shortest_path(node,goal):
    visited = set()
    graph = makeGraph(edges)
    queue = [[node,0]]
  
    while queue:
        
        [current,dist] = queue.pop(0)
        print(current,dist)
        neighbours = graph[current]

        dist += 1
        for n in neighbours:

            
            if n == goal: return dist
            queue.append([n,dist])
    return ('path doesnt exist')

def makeGraph(edges):
    graph = {}
    for [e1,e2] in edges:
        if not(e1 in graph): graph[e1]=[]
        if not(e2 in graph): graph[e2]=[]

        graph[e1].append(e2)
        graph[e2].append(e1)

    print('The adjacency list is',graph)
    return graph

print(shortest_path('w','z'))