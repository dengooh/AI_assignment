from board import Board
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


class Visualizer(Board):
    def __init__(self, board, square_size, start, goal):
        self.board = board
        # Initialize Pygame
        pygame.init()

        # Set square size
        self.square_size = square_size
        self.rows = board.get_rows()
        self.cols = board.get_cols()

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

        # Set start position
        self.grid = board.get_grid()
        self.start = start
        self.grid[start[1]][start[0]] = 'S'

        # Set goal positions
        self.goal = goal
        for pos in self.goal:
            self.grid[pos[1]][pos[0]] = 'G'

    def visualize_search(self, current=None, visited=None, container=None):
        self.screen.fill(self.background_color)

        # First, draw all grid cells
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                color = self.background_color  # Default color for empty cells

                if self.grid[row][col] == 'X':  # Wall
                    color = self.wall_color
                elif self.grid[row][col] == 'S':  # Start
                    color = self.start_color
                elif self.grid[row][col] == 'G':  # Goal
                    color = self.goal_color

                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border

        if visited is not None:
            for pos in visited:
                rect = pygame.Rect(pos[0] * self.square_size, pos[1] * self.square_size, self.square_size,
                                   self.square_size)
                pygame.draw.rect(self.screen, (64, 224, 208), rect)  # Use a color for visited nodes

        # Finally, highlight the current position if available
        if current is not None:
            rect = pygame.Rect(current[0] * self.square_size, current[1] * self.square_size, self.square_size,
                               self.square_size)
            pygame.draw.rect(self.screen, (255, 165, 0), rect)  # Orange for the current position

        # Data extraction from both stack type data structure and a tuple type data structure.
        if container:
            for item in container:
                # Extract position based on item structure.
                if isinstance(item, tuple):
                    if isinstance(item[1], tuple) and len(item[1]) == 2:
                        pos = item[1]  # Priority queue scenario: (priority, (x, y))
                    elif isinstance(item[0], tuple) and len(item[0]) == 2:
                        pos = item[0]  # Scenario where item is (current_position, path_to_current)
                    else:
                        print(f"Unhandled item format: {item}")
                        continue  # Skip this item
                else:
                    print(f"Item is not a tuple, check container structure: {item}")
                    continue  # Skip this item

                # Now, pos should be a valid position (x, y)
                try:
                    queue_rect = pygame.Rect(pos[0] * self.square_size, pos[1] * self.square_size, self.square_size,
                                             self.square_size)
                    pygame.draw.rect(self.screen, (0, 0, 200), queue_rect)  # Dark blue color for position
                except TypeError as e:
                    print(f"Error drawing for {item}: {e}")

        # Redraw grid borders after everything else to ensure visibility (DURING SEARCH)
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border with grid color

    def finish_path(self, path=None):

        if path is not None:
            for pos in path:
                rect = pygame.Rect(pos[0] * self.square_size, pos[1] * self.square_size, self.square_size,
                                   self.square_size)
                pygame.draw.rect(self.screen, (147, 112, 219), rect)  # Use a different color for the path

                for row in range(self.rows):
                    for col in range(self.cols):
                        rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size,
                                           self.square_size)
                        if self.grid[row][col] == 'S':  # Start
                            color = self.start_color
                            pygame.draw.rect(self.screen, color, rect)

                        # Redraw grid borders after everything else to ensure visibility
                for row in range(self.rows):
                    for col in range(self.cols):
                        rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size,
                                           self.square_size)
                        pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border with grid color

                pygame.display.flip()
                pygame.time.delay(100)

    def run_visualization(self, search_method):
        path_found = False
        path = []

        try:
            while True:
                current_pos, path, visited, path_found, container = next(search_method)

                # Clear the screen and update the visualization based on current_pos, path, and visited
                self.visualize_search(current=current_pos, visited=visited, container=container)
                # Handle Pygame events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                pygame.display.flip()
                pygame.time.delay(100)  # Adjust delay for search visualization
        except StopIteration:
            pass  # BFS search is complete

        self.finish_path(path=path if path_found else None)

        # Redraw grid borders after everything else to ensure visibility
        for row in range(self.rows):
            for col in range(self.cols):
                rect = pygame.Rect(col * self.square_size, row * self.square_size, self.square_size, self.square_size)
                pygame.draw.rect(self.screen, self.grid_color, rect, 1)  # Draw border with grid color

        waiting_for_close = True
        while waiting_for_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_close = False
