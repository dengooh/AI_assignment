import sys


class TermInput:
    def __init__(self):
        # self.grid_rows = grid_rows
        # self.grid_cols = grid_cols
        self.filename = sys.argv[1]
        self.method = sys.argv[2]

    def get_grid_size(self):
        # filename = sys.argv[1]
        # method = sys.argv[2]

        with open(self.filename, 'r') as file:
            line = file.readline().strip()

        grid_size_str = line.replace('[', '').replace(']', '')
        grid_size = (list(map(int, grid_size_str.split(','))))

        grid_rows, grid_cols = grid_size[0], grid_size[1]

        return grid_rows, grid_cols

    def get_initial_state(self):
        with open(self.filename, 'r') as file:
            next(file)

            line = file.readline().strip()

        initial_state_str = line.replace('(', '').replace(')', '')
        initial_state = list(map(int, initial_state_str.split(',')))

        return initial_state
