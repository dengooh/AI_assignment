# from board import Board
# from bfs import BFS
# from dfs import DFS
# from gbfs import GBFS
# from astar import AS
from terminput import TermInput
import sys

if __name__ == "__main__":
#     grid_rows, grid_cols = 5, 11
#     initial_state = (0, 1)
#     goal_state = [(7, 0), (10, 3)]
#     walls = [
#         (2, 0, 2, 2),
#         (8, 0, 1, 2),
#         (10, 0, 1, 1),
#         (2, 3, 1, 2),
#         (3, 4, 3, 1),
#         (9, 3, 1, 1),
#         (8, 4, 2, 1)
#         ]

    get_grid_size = TermInput.get_grid_size()
    print(get_grid_size)

    # grid_rows, grid_cols = 8, 15
    # initial_state = (0, 2)
    # goal_state = [(7, 0), (0, 6)]
    # walls = [
    #     (2, 0, 3, 2),
    #     (8, 0, 1, 3),
    #     (14, 0, 1, 2),
    #     (2, 3, 1, 3),
    #     (3, 5, 3, 1),
    #     (9, 4, 1, 2),
    #     (13, 4, 2, 1),
    #     (0, 7, 5, 1),
    #     (7, 7, 5, 1),
    #     (5, 2, 1, 4),
    #     (11, 1, 1, 4)
    # ]

    # grid_rows, grid_cols = 40, 80  # Expanded grid dimensions
    # initial_state = (0, 3)  # Starting point adjusted for the larger grid
    #
    # # Multiple distant goal states to challenge pathfinding over vast distances
    # goal_state = [(75, 0), (79, 39), (0, 39), (40, 20)]
    #
    # # An extensive set of walls, manually defined for a highly complex maze
    # walls = [
    #     (1, 1, 78, 1),  # Top horizontal wall, leaving the corners open
    #     (1, 38, 78, 1),  # Bottom horizontal wall, leaving the corners open
    #     (79, 2, 1, 36),  # Right vertical wall, leaving the top and bottom open
    #
    #     # A series of vertical walls spaced two columns apart
    #     (2, 2, 1, 35), (4, 2, 1, 35), (6, 2, 1, 35), (8, 2, 1, 35),
    #     (10, 2, 1, 35), (12, 2, 1, 35), (14, 2, 1, 35), (16, 2, 1, 35),
    #     (18, 2, 1, 35), (20, 2, 1, 35), (22, 2, 1, 35), (24, 2, 1, 35),
    #     (26, 2, 1, 35), (28, 2, 1, 35), (30, 2, 1, 35), (32, 2, 1, 35),
    #     (34, 2, 1, 35), (36, 2, 1, 35), (38, 2, 1, 35), (40, 2, 1, 35),
    #     (42, 2, 1, 35), (44, 2, 1, 35), (46, 2, 1, 35), (48, 2, 1, 35),
    #     (50, 2, 1, 35), (52, 2, 1, 35), (54, 2, 1, 35), (56, 2, 1, 35),
    #     (58, 2, 1, 35), (60, 2, 1, 35), (62, 2, 1, 35), (64, 2, 1, 35),
    #     (66, 2, 1, 35), (68, 2, 1, 35), (70, 2, 1, 35), (72, 2, 1, 35),
    #     (74, 2, 1, 35), (76, 2, 1, 35),
    #
    #     # Horizontal walls at varying intervals to create complex pathways
    #     (3, 4, 74, 1), (3, 8, 74, 1), (3, 12, 74, 1), (3, 16, 74, 1),
    #     (3, 20, 74, 1), (3, 24, 74, 1), (3, 28, 74, 1), (3, 32, 74, 1),
    #     (3, 36, 74, 1),
    # ]

    # board = Board(grid_rows, grid_cols, walls)
    #
    # bfs = BFS(board, initial_state, goal_state)
    # dfs = DFS(board, initial_state, goal_state)
    # gbfs = GBFS(board, initial_state, goal_state)
    # astar = AS(board, initial_state, goal_state)
    #
    # bfs_path, bfs_directions, bfs_visited, bfs_goal = bfs.find_path()
    # dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()
    # gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()
    # astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()
    #
    # print("Path found with BFS approach: ", bfs_path)
    # print("Direction found with BFS: ", bfs_directions)
    # print("Visited: ", bfs_visited)
    # print("Goal node: ", bfs_goal)
    #
    # print("Path found with DFS approach: ", dfs_path)
    # print("Direction found with DFS: ", dfs_directions)
    # print("Visited: ", dfs_visited)
    # print("Goal node: ", dfs_goal)
    #
    # print("Path found with GBFS approach: ", gbfs_path)
    # print("Direction found with GBFS: ", gbfs_directions)
    # print("Visited: ", gbfs_visited)
    # print("Goal node: ", gbfs_goal)
    #
    # print("Path found with ASTAR approach: ", astar_path)
    # print("Direction found with ASTAR: ", astar_directions)
    # print("Visited: ", astar_visited)
    # print("Goal node: ", astar_goal)