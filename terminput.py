import sys


class TermInput:
    def __init__(self, grid_rows, grid_cols):
        self.grid_rows = grid_rows
        self.grid_cols = grid_cols

    @staticmethod
    def get_grid_size():
        filename = sys.argv[1]
        method = sys.argv[2]

        with open(filename, 'r') as file:
            grid = file.readline().strip()

        grid_size_str = grid.replace('[', '').replace(']', '')
        grid_size = (list(map(int, grid_size_str.split(','))))

        grid_rows, grid_cols = grid_size[0], grid_size[1]

        return grid_rows, grid_cols

