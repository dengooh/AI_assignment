from search_algorithm import SearchAlgorithm, DIRECTIONS
from collections import deque


# Inherits from SearchAlgorithm
class BFS(SearchAlgorithm):
    def __init__(self, board, start, goal_state):
        super().__init__(board, start, goal_state)

    # Perform BFS to find a path from start to one of the goal states
    def find_path(self):
        # Initialize the queue for BFS with the start position
        queue = deque([self.start])
        # Keep track of visited cells to prevent repetition
        visited = {self.start}
        # Record the path taken to reach each cell
        path = {self.start: None}

        # Process each cell in the queue
        while queue:
            current = queue.popleft()
            if current in self.goal_state:
                return self.reconstruct_path(path, current, visited)

            x, y = current
            # the current node is assumed to be a tuple (or list) of two elements representing its position on the board
            for dx, dy in DIRECTIONS:
                # iterates over a predefined list 'DIRECTIONS', which contains tuples representing possible movement --
                # directions from any given node. Goes by the order of UP, LEFT, DOWN, and RIGHT.
                next_x, next_y = x + dx, y + dy
                # calculates the coordinates of the neighboring node in the direction specified by 'dx' and 'dy'. --
                # this is done by adding 'dx' to the current 'x' position and 'dy' to the current 'y' position.
                if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    # checks two conditions before considering a neighbor for exploration: first, whether the cell --
                    # at '(next_x, next_y)' is free (not a wall, as determined by the 'is_free' method of the 'board' --
                    # object), and second, whether this cell has not been visited already. This prevents the --
                    # algorithm from looping indefinitely and ensures it doesn't traverse the walls.
                    visited.add((next_x, next_y))
                    # marks the neighbor node as visited by adding its coordinates to the 'visited' set. --
                    # this prevents the algorithm from processing a node more than once.
                    queue.append((next_x, next_y))
                    # adds neighbor node to the queue, so it will be processed in future iterations of the loop. --
                    # this is how BFS ensures that it explores all nodes level by level.
                    path[(next_x, next_y)] = current
                    # records the current node as the predecessor of the neighbor node in the 'path' dictionary. --
                    # this is essential for reconstructing the path once a goal state is reached. When the goal is --
                    # found, you can trace back from the goal to the start node using this dictionary, effectively --
                    # reconstructing the path taken.

        # If no path is found, return None.
        return None
