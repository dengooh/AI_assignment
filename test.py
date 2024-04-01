Graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    "d": ['f'],
    'e': [],
    'f': []
}


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


print(DFS(Graph, 'a'))