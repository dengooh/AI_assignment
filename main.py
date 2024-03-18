
from board import Board
from bfs import BFS
# import sys

# filename = sys.argv[1]
# method = sys.argv[2]
#
#
# with open(filename) as f:
#     for line in f:
#         print(line)


# Graph = {
#     'a': ['c', 'b'],
#     'b': ['d'],
#     'c': ['e'],
#     "d": ['f'],
#     'e': [],
#     'f': []
# }


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


# def BFS(graph, start):
#     visited = []
#     queue = deque([start])
#     while queue:
#         current = queue.popleft()
#         if current not in visited:
#             visited.append(current)
#
#         for neighbor in graph[current]:
#             queue.append(neighbor)
#
#     return visited
#

# def DFS(graph, start):
#     visited = []
#     stack = [start]
#     while len(stack) > 0:
#         node = stack.pop()
#         if node not in visited:
#             visited.append(node)
#
#         for neighbor in graph[node]:
#             stack.append(neighbor)
#
#     return visited
#
#
# arrayFromRecursiveDFS = []
#
#
# def recursiveDFS(graph, start):
#     arrayFromRecursiveDFS.append(start)
#     for neighbor in graph[start]:
#         recursiveDFS(graph, neighbor)

#
# print("search by DFS: ", DFS(Graph, 'a'))
# recursiveDFS(Graph, 'a')
# print(arrayFromRecursiveDFS)
# print(BFS(Graph, 'a'))
#
# ROW = 2
# COL = 3
#
# board = [ROW][COL]


grid_rows, grid_cols = 5, 11
initial_state = (0, 1)
goal_states = [(7, 0), (10, 3)]
walls = [
    (2, 0, 2, 2),
    (8, 0, 1, 2),
    (10, 0, 1, 1),
    (2, 3, 1, 2),
    (3, 4, 3, 1),
    (9, 3, 1, 1),
    (8, 4, 2, 1)
]

grid = Board(grid_rows, grid_cols, walls)
bfs = BFS(grid, initial_state, goal_states)

path, directions = bfs.find_path()
print("Path found with BFS approach: ", path)
print(directions)