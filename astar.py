from search_algorithm import SearchAlgorithm, DIRECTIONS
from heapq import heappush, heappop


class AS(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    def find_path(self):
        # Open set contains nodes to be evaluated, as (F cost, node) tuples
        open_set = []
        heappush(open_set, (0 + self.heuristic(self.start), self.start))

        path = {self.start: None}
        # Cost from start to the current node
        g_score = {self.start: 0}
        visited = set()

        while open_set:
            current_priority, current = heappop(open_set)

            if current in self.goal:
                return self.reconstruct_path(path, current, visited)

            x, y = current
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if not self.board.is_free(next_x, next_y):
                    continue

                # Assume cost between nodes is 1
                tentative_g_score = g_score[current] + 1
                next_node = (next_x, next_y)
                visited.add((next_x, next_y))

                if next_node not in g_score or tentative_g_score < g_score[next_node]:
                    # This path to the neighbor is better than any previous one
                    path[next_node] = current
                    g_score[next_node] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(next_node)
                    heappush(open_set, (f_score, next_node))

        return None, None, len(visited), "No goal is reachable"