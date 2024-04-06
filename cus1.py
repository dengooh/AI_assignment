from search_algorithm import SearchAlgorithm, DIRECTIONS
from visualizer import Visualizer
import pygame


class CUS1(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    def find_path(self, limit):
        stack = [(self.start, 0)]  # Stack elements representing (node, depth)
        visited = {self.start}
        path = {self.start: None}

        while stack:
            current, depth = stack.pop()

            if current in self.goal:
                return self.reconstruct_path(path, current, visited)

            # Stop expanding this branch if the depth limit is reached
            if depth == limit:
                continue

            x, y = current

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                next_node = (next_x, next_y)

                if self.board.is_free(next_x, next_y) and next_node not in visited:
                    visited.add(next_node)
                    # Append the next node to the stack along with its depth
                    stack.append((next_node, depth + 1))
                    path[next_node] = current

        return None, None, len(visited), "No goal is reachable"


class CUS1_GUI(Visualizer):
    def __init__(self, board, square_size, start, goal):
        super().__init__(board, square_size, start, goal)
        pygame.display.set_caption("Depth Limited Search Pathfinding Visualizer")

    def find_path(self, limit):
        stack = [(self.start, [self.start], 0)]
        visited = {self.start}

        while stack:
            current, path, depth = stack.pop()
            yield current, path, visited, True, stack

            if current in self.goal:
                yield current, path, visited, True, stack
                return

            if depth < limit:
                x, y = current

                for dx, dy in DIRECTIONS:
                    next_x, next_y = x + dx, y + dy

                    if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        # Include the updated depth in the stack elements
                        stack.append(((next_x, next_y), path + [(next_x, next_y)], depth + 1))

            self.visualize_search()

        yield None, None, visited, False, stack