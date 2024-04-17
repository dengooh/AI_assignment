from search_algorithm import SearchAlgorithm, DIRECTIONS
from collections import deque
from visualizer import Visualizer
import pygame


# inherits from SearchAlgorithm
class BFS(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    # perform BFS to find a path from start to one of the goal states
    def find_path(self):
        # initialize the queue for BFS with the start position
        queue = deque([self.start])
        # keep track of visited cells for repeated state check
        visited = {self.start}
        path = {self.start: None}

        while queue:
            current = queue.popleft()
            if current in self.goal:
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

        # if no path is found, return None.
        return None, None, len(visited), "No goal is reachable"


class BFS_GUI(Visualizer):
    def __init__(self, board, square_size, start, goal):
        super().__init__(board, square_size, start, goal)
        pygame.display.set_caption("Breadth First Search Pathfinding Visualizer")

    def find_path(self):
        queue = deque([(self.start, [self.start])])  # Queue of (position, path) tuples
        visited = {self.start}

        while queue:
            current_pos, path = queue.popleft()

            yield current_pos, path, visited, True, queue
            # If current position is a goal, return the path
            if current_pos in self.goal:
                yield current_pos, path, visited, True, queue
                return

            x, y = current_pos

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                # if 0 <= next_pos[0] < self.cols and 0 <= next_pos[1] < self.rows:  # Check bounds
                #     if next_pos not in visited and self.grid[next_pos[1]][next_pos[0]] != 'X':  # Check if walkable
                if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append(((next_x, next_y), path + [(next_x, next_y)]))

            # visualize the current state of the search
            self.visualize_search()

        # return []
        yield None, None, visited, False, queue  # false indicates no path was found