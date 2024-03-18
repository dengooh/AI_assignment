# Define the movement directions in the order UP, LEFT, DOWN, RIGHT.
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class SearchAlgorithm:
    def __init__(self, grid, start, goal_states):
        self.grid = grid
        self.start = start
        self.goal_states = goal_states

    def find_path(self):
        return None

    @staticmethod
    def reconstruct_path(path, goal):
        current = goal
        path_taken = [current]
        directions_taken = []

        # Define the inverse of the movement directions to translate positions to directions
        direction_names = {(0, -1): 'UP', (-1, 0): 'Left', (0, 1): 'DOWN', (1, 0): 'RIGHT'}

        # Follow the recorded path back to the start state.
        while path.get(current) is not None:
            prev = path[current]
            path_taken.append(prev)

            # Computer the direction taken and add it to the directions list.
            dx, dy = current[0] - prev[0], current[1] - prev[1]
            directions_taken.append(direction_names[(dx, dy)])

            current = prev

        # Reverse the path and directions, so they start at the start state and end at the goal.
        path_taken.reverse()
        directions_taken.reverse()
        return path_taken, directions_taken