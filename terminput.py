import sys


class TermInput:
    def __init__(self):
        self.filename = sys.argv[1]
        self.method = sys.argv[2]
        # self.method2 = sys.argv[3]

    # def get_second_method(self):
    #     return self.method2

    def get_method(self):
        return self.method

    def get_grid_size(self):
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
        initial_state = tuple(map(int, initial_state_str.split(',')))

        return initial_state

    def get_goal_state(self):
        goal_coordinates = []
        with open(self.filename, 'r') as file:
            next(file)
            next(file)
            line = file.readline().strip().split(' | ')

        for i in line:
            goal_state_str = i.replace('(', '').replace(')', '')
            goal_state = tuple(map(int, goal_state_str.split(',')))
            goal_coordinates.append(goal_state)

        return goal_coordinates

    def get_walls(self):
        walls_coordinates = []
        with open(self.filename, 'r') as file:
            next(file)
            next(file)
            next(file)
            lines = file.readlines()

        for i in lines:
            walls_str = i.replace('(', '').replace(')', '')
            walls = tuple(map(int, walls_str.split(',')))
            walls_coordinates.append(walls)

        return walls_coordinates

