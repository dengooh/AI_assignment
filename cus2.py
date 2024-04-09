from search_algorithm import SearchAlgorithm, DIRECTIONS


class CUS2(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    def find_path(self):
        def search(path, g, threshold, path_back):
            current = path[-1]
            f = g + self.heuristic(current, self.goal)
            if f > threshold:
                return f, False
            if current == self.goal:
                # When the goal is found, use reconstruct_path to build the full path and directions
                full_path, directions, visited_count, _ = self.reconstruct_path(path_back, current, visited)
                return (full_path, directions), True

            minimum = float('inf')
            for dx, dy in DIRECTIONS:
                next_x, next_y = current[0] + dx, current[1] + dy
                next_node = (next_x, next_y)
                if next_node in visited or not self.board.is_free(next_x, next_y):
                    continue

                if next_node not in path:  # Avoid cycles
                    visited.add(next_node)
                    path.append(next_node)
                    path_back[next_node] = current
                    temp, found = search(path, g + 1, threshold, path_back)
                    if found:
                        return temp, True
                    if temp < minimum:
                        minimum = temp
                    path.pop()
                    visited.remove(next_node)

            return minimum, False

        threshold = self.heuristic(self.start, self.goal)
        path = [self.start]
        visited = {self.start}
        path_back = {self.start: None}
        while True:
            temp, found = search(path, 0, threshold, path_back)
            if found:
                return temp  # Path found
            if temp == float('inf'):
                return None, None, 0, "No goal is reachable"
            threshold = temp