from search_algorithm import SearchAlgorithm, DIRECTIONS
from heapq import heappush, heappop


class GBFS(SearchAlgorithm):
    def __init__(self, board, start, goal_state):
        super().__init__(board, start, goal_state)

    def find_path(self):
        # this list will be used as a priority queue where nodes to be explored are stored along with their priorities
        open_set = []
        # adds teh starting node to the 'open_set' with a priority of '0'
        heappush(open_set, (0, self.start))
        # maps each node to its predecessor on the shortest path found so far. The start node doesn't have a --
        # predecessor, hence it's mapped to 'None'
        path = {self.start: None}

        while open_set:
            # removes and returns the node with the highest priority (lowest value) from the 'open_set' --
            # this operation also maintains the heap property. 'current' is the node to be explored next, and --
            # 'current-property' is its priority
            current_priority, current = heappop(open_set)

            if current in self.goal_state:
                return self.reconstruct_path(path, current)

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
                    if next_step not in path:
                        # calculates the priority of the neighboring node using the heuristic function. This priority --
                        # is typically a measure of how close the node is to the goal
                        priority = self.heuristic(next_step)
                        # adds the neighboring node to the 'open_set' with its calculated priority, ensuring the node --
                        # will be explored in an order determined by its priority
                        heappush(open_set, (priority, next_step))
                        # records the current node as the predecessor of the neighbor. need for path reconstruction
                        path[next_step] = current

        return None
