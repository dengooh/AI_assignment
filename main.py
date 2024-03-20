from board import Board
from bfs import BFS
from dfs import DFS
from gbfs import GBFS
from astar import AS

# import sys

# filename = sys.argv[1]
# method = sys.argv[2]
#
#
# with open(filename) as f:
#     for line in f:
#         print(line)


if __name__ == "__main__":
    grid_rows, grid_cols = 5, 11
    initial_state = (0, 1)
    goal_state = [(7, 0), (10, 3)]
    walls = [
        (2, 0, 2, 2),
        (8, 0, 1, 2),
        (10, 0, 1, 1),
        (2, 3, 1, 2),
        (3, 4, 3, 1),
        (9, 3, 1, 1),
        (8, 4, 2, 1)
    ]

    board = Board(grid_rows, grid_cols, walls)

    bfs = BFS(board, initial_state, goal_state)
    dfs = DFS(board, initial_state, goal_state)
    gbfs = GBFS(board, initial_state, goal_state)
    astar = AS(board, initial_state, goal_state)

    bfs_path, bfs_directions = bfs.find_path()
    dfs_path, dfs_directions = dfs.find_path()
    gbfs_path, gbfs_directions = gbfs.find_path()
    astar_path, astar_directions = astar.find_path()

    print("Path found with BFS approach: ", bfs_path)
    print("Direction found with BFS: ", bfs_directions)

    # print("Path found with DFS approach: ", dfs_path)
    # print("Direction found with DFS: ", dfs_directions)
    #
    # print("Path found with GBFS approach: ", gbfs_path)
    # print("Direction found with GBFS: ", gbfs_directions)

    print("Path found with ASTAR approach: ", astar_path)
    print("Direction found with ASTAR: ", astar_directions)



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
