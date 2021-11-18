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

print('has path using DFS recursion')
#check if there is a path using depth first recursion
def hasPath_DF(graph,node,goal):
    if node == goal: return True
    neighbours = graph[node]
    for n in neighbours:
        if hasPath_DF(graph,n,goal):
            return True

    return False

print(hasPath_DF(graph,'a','e'))
print(hasPath_DF(graph,'a','k'))

print('has path using BFS recursion')
#check if there is a path using depth first recursion
def hasPath_BF(graph,node,goal):
    queue = [node]
    
    while queue:
        neighbours = graph[queue.pop(0)]
        for n in neighbours:
            if n==goal: return True
            queue.append(n)
    return False
print(hasPath_BF(graph,'a','k'))
print(hasPath_BF(graph,'a','e'))