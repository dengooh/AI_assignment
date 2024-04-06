from board import Board
from bfs import BFS, BFS_GUI
from dfs import DFS, DFS_GUI
from gbfs import GBFS, GBFS_GUI
from astar import AS, AS_GUI
from terminput import TermInput
from cus1 import CUS1, CUS1_GUI


if __name__ == "__main__":

    TI = TermInput()

    grid_rows = TI.get_grid_size()[0]
    grid_cols = TI.get_grid_size()[1]
    start = TI.get_initial_state()
    goal = TI.get_goal_state()
    walls = TI.get_walls()

    board = Board(grid_rows, grid_cols, walls)

    match TI.get_method():
        case 'BFS':
            bfs = BFS(board, start, goal)
            bfs_path, bfs_directions, bfs_visited, bfs_goal = bfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", bfs_goal)
            print("Visited: ", bfs_visited)
            print("Direction found with BFS: ", bfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                bfs = BFS_GUI(board, 40, start, goal)
                # game = Visualizer()

                bfs.run_visualization(bfs.find_path())

        case 'DFS':
            dfs = DFS(board, start, goal)
            dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", dfs_goal)
            print("Visited: ", dfs_visited)
            print("Direction found with DFS: ", dfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                dfs = DFS_GUI(board, 40, start, goal)

                dfs.run_visualization(dfs.find_path())

        case 'GBFS':
            gbfs = GBFS(board, start, goal)
            gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", gbfs_goal)
            print("Visited: ", gbfs_visited)
            print("Direction found with GBFS: ", gbfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                gbfs = GBFS_GUI(board, 40, start, goal)

                gbfs.run_visualization(gbfs.find_path())

        case 'AS':
            astar = AS(board, start, goal)
            astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", astar_goal)
            print("Visited: ", astar_visited)
            print("Direction found with A-Star: ", astar_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                astar = AS_GUI(board, 40, start, goal)

                astar.run_visualization(astar.find_path())

        case 'CUS1':
            ran = False
            limit = 0

            while not ran:
                try:
                    limit = int(input("Enter the limit (int): "))
                    ran = True
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            dls = CUS1(board, start, goal)
            dls_path, dls_directions, dls_visited, dls_goal = dls.find_path(limit)

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", dls_goal)
            print("Visited: ", dls_visited)
            print("Direction found with DLS: ", dls_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                dls = CUS1_GUI(board, 40, start, goal)

                dls.run_visualization(dls.find_path(limit))

        case 'CUS2':
            pass
