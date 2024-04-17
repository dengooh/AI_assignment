from search_algorithm import SearchAlgorithm, DIRECTIONS
from visualizer import Visualizer
import pygame


# mplemented the same way as BFS, but use a stack memory (FILO)
class DFS(SearchAlgorithm):
    def __init__(self, board, start, goal_state):
        super().__init__(board, start, goal_state)

    def find_path(self):
        stack = [self.start]
        visited = {self.start}
        path = {self.start: None}

        while stack:
            current = stack.pop()

            if current in self.goal:
                return self.reconstruct_path(path, current, visited)

            x, y = current

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    stack.append((next_x, next_y))
                    path[(next_x, next_y)] = current

        # If no path is found, return None
        return None, None, len(visited), "No goal is reachable"


class DFS_GUI(Visualizer):
    def __init__(self, board, square_size, start, goal):
        super().__init__(board, square_size, start, goal)
        pygame.display.set_caption("Depth First Search Pathfinding Visualizer")

    def find_path(self):
        stack = [(self.start, [self.start])]  # queue of (position, path) tuples
        visited = {self.start}

        while stack:
            current_pos, path = stack.pop()
            yield current_pos, path, visited, True, stack

            # if current position is a goal, return the path
            if current_pos in self.goal:
                yield current_pos, path, visited, True, stack
                return

            x, y = current_pos

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    stack.append(((next_x, next_y), path + [(next_x, next_y)]))

            # visualize the current state of the search
            self.visualize_search()

        yield None, None, visited, False, stack