class Board:
    def __init__(self, rows, cols, walls):
        self.rows = rows
        self.cols = cols
        # Initializing the NxM grid
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.place_walls(walls)

    # Place walls onto the grid based on the provided list of wall specifications
    def place_walls(self, walls):
        # x, y, w, and h represent the parameters of a wall in the grid
        for x, y, w, h in walls:
            # 'x': The x-coordinate of the leftmost column where the wall starts.
            # 'y': The y-coordinate of the topmost row where the wall starts.
            # 'w': The width of the wall, representing how many columns it extends to the right of the x-coordinate.
            # 'h': The height of the wall, representing how many rows it extends downward from the 'y' coordinate.
            for i in range(h):
                for j in range(w):
                    # Assigning 'X' as walls after the iteration
                    self.grid[y + i][x + j] = 'X'

    # Check if a particular cell is free (not a wall) and within grid boundaries
    def is_free(self, x, y):
        return True if 0 <= y < self.rows and 0 <= x < self.cols and self.grid[y][x] != 'X' else False
        # '0 <= y < self.rows' checks if the y coordinate is within the vertical bounds of the grid.
        # '0 <= y' ensures that y is not negative (it's at least the top row).
        # 'y < self.rows' ensures that y is less than the number of rows in the grid (it's not below the bottom row0

        # '0 <= x < self.cols' checks if the x coordinate is within the horizontal bounds of the grid
        # '0 <= x' ensures that x is not negative (it's at least the leftmost column)
        # 'x < self.cols' ensures that x is less than the number of columns in the grid --
        # (it's not beyond the rightmost column).
