from board import Board
from bfs import BFS
from dfs import DFS
from gbfs import GBFS
from astar import AS
from terminput import TermInput


if __name__ == "__main__":

    TI = TermInput()

    print(TI.get_filename())

    grid_rows = TI.get_grid_size()[0]
    grid_cols = TI.get_grid_size()[1]
    initial_state = TI.get_initial_state()
    goal_state = TI.get_goal_state()
    walls = TI.get_walls()

    board = Board(grid_rows, grid_cols, walls)

    match TI.get_method():
        case 'BFS':
            bfs = BFS(board, initial_state, goal_state)
            bfs_path, bfs_directions, bfs_visited, bfs_goal = bfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", bfs_goal)
            print("Visited: ", bfs_visited)
            print("Direction found with BFS: ", bfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                print("gui")

        case 'DFS':
            dfs = DFS(board, initial_state, goal_state)
            dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", dfs_goal)
            print("Visited: ", dfs_visited)
            print("Direction found with DFS: ", dfs_directions)

        case 'GBFS':
            gbfs = GBFS(board, initial_state, goal_state)
            gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", gbfs_goal)
            print("Visited: ", gbfs_visited)
            print("Direction found with BFS: ", gbfs_directions)

        case 'AS':
            astar = AS(board, initial_state, goal_state)
            astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", astar_goal)
            print("Visited: ", astar_visited)
            print("Direction found with BFS: ", astar_directions)

        case 'CUS1':
            pass

        case 'CUS2':
            pass