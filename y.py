import pygame
import sys

from collections import deque


class GridGame:
    def __init__(self, rows, cols, square_size, start_pos, goal_positions):
        # Initialize Pygame
        pygame.init()

        # Set grid dimensions and square size
        self.rows = rows
        self.cols = cols
        self.square_size = square_size

        # Calculate window size
        self.window_width = self.square_size * self.cols
        self.window_height = self.square_size * self.rows
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.DOUBLEBUF)

        # Colors
        self.background_color = (255, 255, 255)  # White
        self.grid_color = (0, 0, 0)  # Black
        self.wall_color = (128, 128, 128)  # Gray
        self.start_color = (255, 0, 0)  # Green
        self.goal_color = (0, 255, 0)  # Red

        # Create grid
        self.grid = [['' for _ in range(cols)] for _ in range(rows)]

        # Set start position
        self.start_pos = start_pos
        self.grid[start_pos[1]][start_pos[0]] = 'S'

        # Set goal positions
        self.goal_positions = goal_positions
        for pos in self.goal_positions:
            self.grid[pos[1]][pos[0]] = 'G'

    def place_walls(self, walls):
        for x, y, w, h in walls:
            for i in range(h):
                for j in range(w):
                    self.grid[y + i][x + j] = 'X'

    def bfs(self):
        queue = deque([(self.start_pos, [self.start_pos])])  # Queue of (position, path) tuples
        visited = set([self.start_pos])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # UP, DOWN, LEFT, RIGHT

        while queue:
            current_pos, path = queue.popleft()
            yield current_pos, path, visited

            # If current position is a goal, return the path
            if current_pos in self.goal_positions:
                return path

            for dx, dy in directions:
                next_pos = (current_pos[0] + dx, current_pos[1] + dy)

                if 0 <= next_pos[0] < self.cols and 0 <= next_pos[1] < self.rows:  # Check bounds
                    if next_pos not in visited and self.grid[next_pos[1]][next_pos[0]] != 'X':  # Check if walkable
                        visited.add(next_pos)
                        queue.append((next_pos, path + [next_pos]))
                        self.grid[next_pos[1]][next_pos[0]] = 'O'  # Optional: Mark cell as visited for visualization

            # Visualize the current state of the search
            self.visualize_search()
            pygame.time.delay(50)  # Slow down the visualization

        return []  # Return an empty path if no path is found

    def visualize_search(self, current=None, path=None, visited=None):
        self.screen.fill(self.background_color)

        # First, draw all grid cells
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                color = self.grid_color  # Default color for empty cells

                if self.grid[row][col] == 'X':  # Wall
                    color = self.wall_color
                elif self.grid[row][col] == 'S':  # Start
                    color = self.start_color
                elif self.grid[row][col] == 'G':  # Goal
                    color = self.goal_color

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border

        # Then, highlight visited cells if available
        if visited is not None:
            for pos in visited:
                rect = pygame.Rect(pos[0] * self.square_size, pos[1] * self.square_size, self.square_size,
                                   self.square_size)
                pygame.draw.rect(self.screen, (64, 224, 208), rect)  # Use a color for visited nodes

        # Next, draw the path if available
        if path is not None:
            print(path)
            for pos in path:
                rect = pygame.Rect(pos[0] * self.square_size, pos[1] * self.square_size, self.square_size,
                                   self.square_size)
                pygame.draw.rect(self.screen, (147, 112, 219), rect)  # Use a different color for the path

        # Finally, highlight the current position if available
        if current is not None:
            rect = pygame.Rect(current[0] * self.square_size, current[1] * self.square_size, self.square_size,
                               self.square_size)
            pygame.draw.rect(self.screen, (255, 165, 0), rect)  # Orange for the current position

        # Redraw grid borders after everything else to ensure visibility
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border with grid color

        pygame.display.flip()

    def run_bfs_visualization(self):
        bfs_generator = self.bfs()
        try:
            while True:
                current_pos, path, visited = next(bfs_generator)

                # Clear the screen and update the visualization based on current_pos, path, and visited
                self.visualize_search(current=current_pos, path=path, visited=visited)

                # Handle Pygame events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                pygame.display.flip()
                pygame.time.delay(1000)  # Adjust delay as needed
        except StopIteration:
            pass  # BFS search is complete

        waiting_for_close = True
        while waiting_for_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_close = False

        pygame.quit()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.background_color)

            # Draw the grid, walls, start, and goals
            for row in range(self.rows):
                for col in range(self.cols):
                    rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size,
                                       self.square_size)

                    if self.grid[row][col] == 'X':  # Wall
                        pygame.draw.rect(self.screen, self.wall_color, rect)
                    elif self.grid[row][col] == 'S':  # Start
                        pygame.draw.rect(self.screen, self.start_color, rect)
                    elif self.grid[row][col] == 'G':  # Goal
                        pygame.draw.rect(self.screen, self.goal_color, rect)

                    # Redraw the border for clarity
                    pygame.draw.rect(self.screen, self.grid_color, rect, 1)

            pygame.display.flip()

        pygame.quit()
        sys.exit()


# Example usage
if __name__ == "__main__":
    # Define start position and multiple goal positions as (x, y)
    start_pos = (0, 1)
    goal_positions = [(7, 0), (10, 3)]  # Multiple goal positions
    game = GridGame(5, 11, 40, start_pos, goal_positions)

    # Example walls (x, y, width, height)
    walls = [(2,0,2,2),
            (8,0,1,2),
            (10,0,1,1),
            (2,3,1,2),
            (3,4,3,1),
            (9,3,1,1),
            (8,4,2,1)]
    game.place_walls(walls)

    game.run_bfs_visualization()