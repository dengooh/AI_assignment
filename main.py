from board import Board
from bfs import BFS, BFS_GUI
from dfs import DFS, DFS_GUI
from gbfs import GBFS, GBFS_GUI
from astar import AS, AS_GUI
from terminput import TermInput


if __name__ == "__main__":

    TI = TermInput()

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
                board = Board(grid_rows, grid_cols, walls)
                bfs = BFS_GUI(board, 40, initial_state, goal_state)
                # game = Visualizer()

                bfs.run_visualization(bfs.bfs_gui())

        case 'DFS':
            dfs = DFS(board, initial_state, goal_state)
            dfs_path, dfs_directions, dfs_visited, dfs_goal = dfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", dfs_goal)
            print("Visited: ", dfs_visited)
            print("Direction found with DFS: ", dfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                dfs = DFS_GUI(board, 40, initial_state, goal_state)
                # game = Visualizer()

                dfs.run_visualization(dfs.dfs_gui())
                # dfs.finish_path(dfs_path)

        case 'GBFS':
            gbfs = GBFS(board, initial_state, goal_state)
            gbfs_path, gbfs_directions, gbfs_visited, gbfs_goal = gbfs.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", gbfs_goal)
            print("Visited: ", gbfs_visited)
            print("Direction found with GBFS: ", gbfs_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                gbfs = GBFS_GUI(board, 40, initial_state, goal_state)
                # game = Visualizer()

                gbfs.run_visualization(gbfs.gbfs_gui())

        case 'AS':
            astar = AS(board, initial_state, goal_state)
            astar_path, astar_directions, astar_visited, astar_goal = astar.find_path()

            print(TI.get_filename() + " " + TI.get_method())
            print("Goal node: ", astar_goal)
            print("Visited: ", astar_visited)
            print("Direction found with BFS: ", astar_directions)

            if TI.get_second_method() is not None and TI.get_second_method() == 'GUI':
                board = Board(grid_rows, grid_cols, walls)
                astar = AS_GUI(board, 40, initial_state, goal_state)
                # game = Visualizer()

                astar.run_visualization(astar.as_gui())

        case 'CUS1':
            pass

        case 'CUS2':
            pass
