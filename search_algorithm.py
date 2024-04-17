# define the movement directions in the order UP, LEFT, DOWN, RIGHT.
DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]


class SearchAlgorithm:
    def __init__(self, board, start, goal):
        self.board = board
        self.start = start
        self.goal = goal

    @staticmethod
    def reconstruct_path(path, current, visited):
        # initializes 'current' with the goal node.
        # current = goal
        # initializes a list 'path_taken' with the current node (initially the goal node). This list will store the --
        # sequence of nodes visited on the path from the start node to the goal node, in reverse order initially.
        path_taken = [current]
        # initializes an empty list 'directions_taken' that will store the directions taken to move from node to node --
        # along the path, translated into human-readable directions like 'UP, 'DOWN', etc.
        directions_taken = []

        # maps the differences in coordinates between a node and its predecessor to the corresponding direction names.
        direction_names = {(0, -1): 'UP', (-1, 0): 'Left', (0, 1): 'DOWN', (1, 0): 'RIGHT'}

        # follow the recorded path back to the start state.
        # while path.get(current) is not None:
        while current in path and path[current] is not None:
            # retrieves the predecessor of the current node and stores it in 'prev'
            prev = path[current]
            # adds the predecessor node to the 'path_taken' list. This builds up the path from the goal node back to --
            # the start node
            path_taken.append(prev)

            # calculates the differences in the x and y coordinates between the current node and its predecessor. --
            # these differences indicate the direction of movement from 'prev' to 'current'
            dx, dy = current[0] - prev[0], current[1] - prev[1]
            # translate the coordinate differences into a direction using the 'direction_names' dictionary and appends -
            # this direction to the 'directions_taken' list.
            directions_taken.append(direction_names[(dx, dy)])

            # sets 'current' to its predecessor, moving one step closer to the start node in the backtracking process
            current = prev

        # reverse the path and directions, so they start at the start state and end at the goal.
        path_taken.reverse()
        # reverse the 'directions_taken' list for the same reason, so the directions are in the order they were --
        # taken from start to goal
        directions_taken.reverse()

        return path_taken, directions_taken, len(visited), path_taken[-1]

    @staticmethod
    def reconstruct_path_gui(path, current):
        # reconstruct the path from the goal to the start
        reconstructed_path = []
        while current in path:
            reconstructed_path.append(current)
            current = path[current]
        reconstructed_path.reverse()  # the path is built from goal to start; reverse it
        return reconstructed_path

    @staticmethod
    def heuristic(current, goal):
        # manhattan distance to the closest goal_state
        # (return the x, y distances coordinates between the current and the goal nodes)
        return min(abs(current[0] - goal_state[0]) + abs(current[1] - goal_state[1]) for goal_state in goal)
