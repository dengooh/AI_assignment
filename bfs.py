from search_algorithms import SearchAlgorithm, DIRECTIONS
from collections import deque


class BFS(SearchAlgorithm):
    def __init__(self, grid, start, goal_states):
        super().__init__(grid, start, goal_states)

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
            if current in self.goal_states:
                return SearchAlgorithm.reconstruct_path(path, current)

            x, y = current
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy
                if self.grid.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y))
                    path[(next_x, next_y)] = current

        # If no path is found, return None.
        return None
