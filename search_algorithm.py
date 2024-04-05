# Define the movement directions in the order UP, LEFT, DOWN, RIGHT.
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class SearchAlgorithm:
    def __init__(self, board, start, goal):
        self.board = board
        self.start = start
        self.goal = goal

    def find_path(self):
        pass

    @staticmethod
    def reconstruct_path(path, current, visited):
        # Initializes 'current' with the goal node.
        # current = goal
        # Initializes a list 'path_taken' with the current node (initially the goal node). This list will store the --
        # sequence of nodes visited on the path from the start node to the goal node, in reverse order initially.
        path_taken = [current]
        # Initializes an empty list 'directions_taken' that will store the directions taken to move from node to node --
        # along the path, translated into human-readable directions like 'UP, 'DOWN', etc.
        directions_taken = []

        # Maps the differences in coordinates between a node and its predecessor to the corresponding direction names.
        direction_names = {(0, -1): 'UP', (-1, 0): 'Left', (0, 1): 'DOWN', (1, 0): 'RIGHT'}

        # Follow the recorded path back to the start state.
        # while path.get(current) is not None:
        while current in path and path[current] is not None:
            # Retrieves the predecessor of the current node and stores it in 'prev'
            prev = path[current]
            # Adds the predecessor node to the 'path_taken' list. This builds up the path from the goal node back to --
            # the start node
            path_taken.append(prev)

            # Calculates the differences in the x and y coordinates between the current node and its predecessor. --
            # These differences indicate the direction of movement from 'prev' to 'current'
            dx, dy = current[0] - prev[0], current[1] - prev[1]
            # Translate the coordinate differences into a direction using the 'direction_names' dictionary and appends -
            # this direction to the 'directions_taken' list.
            directions_taken.append(direction_names[(dx, dy)])

            # Sets 'current' to its predecessor, moving one step closer to the start node in the backtracking process
            current = prev

        # Reverse the path and directions, so they start at the start state and end at the goal.
        path_taken.reverse()
        # Reverse the 'directions_taken' list for the same reason, so the directions are in the order they were --
        # taken from start to goal
        directions_taken.reverse()

        return path_taken, directions_taken, len(visited), path_taken[-1]

    @staticmethod
    def heuristic(current, goal):
        # Manhattan distance to the closest goal_state
        # (return the x, y distances coordinates between the current and the goal nodes)
        return min(abs(current[0] - goal_state[0]) + abs(current[1] - goal_state[1]) for goal_state in goal)
