from search_algorithm import SearchAlgorithm, DIRECTIONS
from heapq import heappush, heappop
from visualizer import Visualizer
import pygame


class AS(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    def find_path(self):
        # priority queue contains nodes to be evaluated, as (F cost, node) tuples
        priority_queue = []
        heappush(priority_queue, (0 + self.heuristic(self.start, self.goal), self.start))

        path = {self.start: None}
        # cost from start to the current node
        g_score = {self.start: 0}
        visited = set()

        while priority_queue:
            current_priority, current = heappop(priority_queue)

            if current in self.goal:
                return self.reconstruct_path(path, current, visited)

            x, y = current
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if not self.board.is_free(next_x, next_y):
                    continue

                # assume cost between nodes is 1
                tentative_g_score = g_score[current] + 1
                next_node = (next_x, next_y)
                visited.add((next_x, next_y))

                if next_node not in g_score or tentative_g_score < g_score[next_node]:
                    # this path to the neighbor is better than any previous one
                    path[next_node] = current
                    g_score[next_node] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(next_node, self.goal)
                    heappush(priority_queue, (f_score, next_node))

        return None, None, len(visited), "No goal is reachable"


class AS_GUI(Visualizer, SearchAlgorithm):
    def __init__(self, board, square_size, start, goal):
        super().__init__(board, square_size, start, goal)
        pygame.display.set_caption("A-Star Pathfinding Visualizer")

    def find_path(self):
        # priority queue contains nodes to be evaluated, as (F cost, node) tuples
        priority_queue = []
        heappush(priority_queue, (0 + self.heuristic(self.start, self.goal), self.start))

        path = {self.start: None}
        # cost from start to the current node
        g_score = {self.start: 0}
        visited = set()

        while priority_queue:
            current_priority, current = heappop(priority_queue)

            yield current, self.reconstruct_path_gui(path, current), visited, True, priority_queue

            if current in self.goal:
                yield current, self.reconstruct_path_gui(path, current), visited, True, priority_queue
                return  # Path found

            x, y = current
            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if not self.board.is_free(next_x, next_y):
                    continue

                # assume cost between nodes is 1
                tentative_g_score = g_score[current] + 1
                next_node = (next_x, next_y)
                visited.add((next_x, next_y))

                if next_node not in g_score or tentative_g_score < g_score[next_node]:
                    # this path to the neighbor is better than any previous one
                    g_score[next_node] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(next_node, self.goal)
                    heappush(priority_queue, (f_score, next_node))
                    path[(next_x, next_y)] = current

            self.visualize_search()

        yield None, None, visited, False, priority_queue