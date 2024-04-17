from board import Board
from bfs import BFS, BFS_GUI
from dfs import DFS, DFS_GUI
from gbfs import GBFS, GBFS_GUI
from astar import AS, AS_GUI
from terminput import TermInput
from cus1 import CUS1, CUS1_GUI
from cus2 import CUS2


if __name__ == "__main__":

    # initialization of terminput class
    TI = TermInput()

    # getting a data and assign it the correct value
    grid_rows = TI.get_grid_size()[0]
    grid_cols = TI.get_grid_size()[1]
    start = TI.get_initial_state()
    goal = TI.get_goal_state()
    walls = TI.get_walls()

    board = Board(grid_rows, grid_cols, walls)

    # switch case statement to know which function to be used and executed.
    match TI.get_method():
        case 'BFS':
            bfs = BFS(board, start, goal)
            bfs_path, bfs_directions, bfs_visited, bfs_goal = bfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", bfs_goal, "| Number of Nodes: ", bfs_visited)
            print("Direction found with BFS: ", bfs_directions, '\n')

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                bfs = BFS_GUI(board, 40, start, goal)

                bfs.draw(bfs.find_path())

        case 'DFS':
            dfs = DFS(board, start, goal)
            dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", dfs_goal, "| Number of Nodes: ", dfs_visited)
            print("Direction found with DFS: ", dfs_directions, '\n')

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                dfs = DFS_GUI(board, 40, start, goal)

                dfs.draw(dfs.find_path())

        case 'GBFS':
            gbfs = GBFS(board, start, goal)
            gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", gbfs_goal, "| Number of Nodes: ", gbfs_visited)
            print("Direction found with GBFS: ", gbfs_directions, '\n')

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                gbfs = GBFS_GUI(board, 40, start, goal)

                gbfs.draw(gbfs.find_path())

        case 'AS':
            astar = AS(board, start, goal)
            astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", astar_goal, "| Number of Nodes: ", astar_visited)
            print("Direction found with A-Star: ", astar_directions, '\n')

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                astar = AS_GUI(board, 40, start, goal)

                astar.draw(astar.find_path())

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
            print("Goal node: ", dls_goal, "| Number of Nodes: ", dls_visited)
            print("Direction found with DLS: ", dls_directions, '\n')

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                dls = CUS1_GUI(board, 40, start, goal)

                dls.draw(dls.find_path(limit))

        case 'CUS2':
            pass
