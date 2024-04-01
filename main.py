from board import Board
from bfs import BFS
from dfs import DFS
from gbfs import GBFS
from astar import AS
from terminput import TermInput


if __name__ == "__main__":

    TI = TermInput()

    grid_rows = TI.get_grid_size()[0]
    grid_cols = TI.get_grid_size()[1]
    initial_state = TI.get_initial_state()
    goal_state = TI.get_goal_state()
    walls = TI.get_walls()

    board = Board(grid_rows, grid_cols, walls)

    bfs = BFS(board, initial_state, goal_state)
    dfs = DFS(board, initial_state, goal_state)
    gbfs = GBFS(board, initial_state, goal_state)
    astar = AS(board, initial_state, goal_state)

    bfs_path, bfs_directions, bfs_visited, bfs_goal = bfs.find_path()
    dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()
    gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()
    astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()

    match TI.get_method():
        case 'BFS':
            print("Path found with BFS approach: ", bfs_path)
            print("Direction found with BFS: ", bfs_directions)
            print("Visited: ", bfs_visited)
            print("Goal node: ", bfs_goal)

            if TI.get_second_method() == 'GUI':
                print('GUI')

        case 'DFS':
            print("Path found with DFS approach: ", dfs_path)
            print("Direction found with DFS: ", dfs_directions)
            print("Visited: ", dfs_visited)
            print("Goal node: ", dfs_goal)

        case 'GBFS':
            print("Path found with GBFS approach: ", gbfs_path)
            print("Direction found with GBFS: ", gbfs_directions)
            print("Visited: ", gbfs_visited)
            print("Goal node: ", gbfs_goal)

        case 'AS':
            print("Path found with ASTAR approach: ", astar_path)
            print("Direction found with ASTAR: ", astar_directions)
            print("Visited: ", astar_visited)
            print("Goal node: ", astar_goal)

        case 'CUS1':
            pass

        case 'CUS2':
            pass