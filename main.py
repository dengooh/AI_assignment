from collections import deque
# import sys
#
# filename = sys.argv[1]
#
# with open(filename) as f:
#     for line in f:
#         print(line)


Graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    "d": ['f'],
    'e': [],
    'f': []
}


# def DFS(graph, start):
#     visited = []
#     stack = [start]
#     while len(stack) > 0:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#             stack.extend(reversed(graph.get(node, [])))
#
#     return visited


def BFS(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)

        for neighbor in graph[current]:
            queue.append(neighbor)

    return visited


def DFS(graph, start):
    visited = []
    stack = [start]
    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            visited.append(node)

        for neighbor in graph[node]:
            stack.append(neighbor)

    return visited


arrayFromRecursiveDFS = []


def recursiveDFS(graph, start):
    arrayFromRecursiveDFS.append(start)
    for neighbor in graph[start]:
        recursiveDFS(graph, neighbor)


print("search by DFS: ", DFS(Graph, 'a'))
recursiveDFS(Graph, 'a')
print(arrayFromRecursiveDFS)
print(BFS(Graph, 'a'))