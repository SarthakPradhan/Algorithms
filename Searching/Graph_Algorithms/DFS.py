graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[],
}
#DF Traversal
print('depth first traversal')
def DFS(graph, start_node):
    stack = [start_node]
    while stack:
        current = stack.pop()
        print(current)
        neighbours = graph[current]
        for n in neighbours:
            stack.append(n)

DFS(graph,'a')

#BF Traversal
print('breadth first traversal')
def BFS(graph, start_node):
    queue = [start_node]
    while queue:
        current = queue.pop(0)
        print(current)
        neighbours = graph[current]
        for n in neighbours:
            queue.append(n)

BFS(graph,'a')