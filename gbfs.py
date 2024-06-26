from search_algorithm import SearchAlgorithm, DIRECTIONS
from heapq import heappush, heappop
from visualizer import Visualizer
import pygame


class GBFS(SearchAlgorithm):
    def __init__(self, board, start, goal):
        super().__init__(board, start, goal)

    def find_path(self):
        # this list will be used as a priority queue where nodes to be explored are stored along with their priorities
        priority_queue = []
        # adds the starting node to the 'priority_queue' with a priority of '0'
        heappush(priority_queue, (0, self.start))
        # maps each node to its predecessor on the shortest path found so far. The start node doesn't have a --
        # predecessor, hence it's mapped to 'None'
        path = {self.start: None}
        visited = set()

        while priority_queue:
            # removes and returns the node with the highest priority (lowest value) from the 'priority_queue' --
            # this operation also maintains the heap property. 'current' is the node to be explored next, and --
            # 'current-property' is its priority
            current_priority, current = heappop(priority_queue)

            if current in self.goal:
                return self.reconstruct_path(path, current, visited)

            # unpacks the current node's coordinate
            x, y = current
            # iterates over 'DIRECTIONS'
            for dx, dy in DIRECTIONS:
                # calculate the coordinates of the neighboring node in each direction
                next_x, next_y = x + dx, y + dy
                # checks if the neighboring node at '(next_x, next_y)' is accessible (not a wall or outside boundaries)
                if self.board.is_free(next_x, next_y):
                    # assigns the coordinates of the neighboring node
                    next_step = (next_x, next_y)
                    visited.add(next_step)
                    if next_step not in path:
                        # calculates the priority of the neighboring node using the heuristic function. This priority --
                        # is typically a measure of how close the node is to the goal
                        priority = self.heuristic(next_step, self.goal)
                        # adds the neighboring node to the 'priority_queue' with its calculated priority, ensuring the node --
                        # will be explored in an order determined by its priority
                        heappush(priority_queue, (priority, next_step))
                        # records the current node as the predecessor of the neighbor. need for path reconstruction
                        path[next_step] = current

        return None, None, len(visited), "No goal is reachable"


class GBFS_GUI(Visualizer, SearchAlgorithm):
    def __init__(self, board, square_size, start, goal):
        super().__init__(board, square_size, start, goal)
        pygame.display.set_caption("Greedy Best First Search Pathfinding Visualizer")

    def find_path(self):
        open_set = []
        heappush(open_set, (0, self.start))
        path = {self.start: None}  # using a dictionary to reconstruct the path
        visited = {self.start}

        while open_set:
            current_priority, current = heappop(open_set)

            yield current, self.reconstruct_path_gui(path, current), visited, True, open_set

            if current in self.goal:
                yield current, self.reconstruct_path_gui(path, current), visited, True, open_set
                return  # path found

            x, y = current

            for dx, dy in DIRECTIONS:
                next_x, next_y = x + dx, y + dy

                if self.board.is_free(next_x, next_y) and (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    priority = self.heuristic((next_x, next_y), self.goal)
                    heappush(open_set, (priority, (next_x, next_y)))
                    path[(next_x, next_y)] = current  # important for path reconstruction

            # slow down the visualization, adjust as needed
            self.visualize_search()

        # if no path is found
        yield None, None, visited, False, open_set