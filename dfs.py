from search_algorithm import SearchAlgorithm, DIRECTIONS


# Implemented the same way as BFS, but use a stack memory (FILO)
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
