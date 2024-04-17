class Board:
    def __init__(self, rows, cols, walls):
        self.rows = rows
        self.cols = cols
        # initializing the NxM grid
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.place_walls(walls)

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_grid(self):
        return self.grid

    # place walls onto the grid
    def place_walls(self, walls):
        # x, y, w, and h represent the parameters of a wall in the grid
        for x, y, w, h in walls:
            # 'x': The x-coordinate of the leftmost column where the wall starts.
            # 'y': The y-coordinate of the topmost row where the wall starts.
            # 'w': The width of the wall, representing how many columns it extends to the
            #  right of the x-coordinate.
            # 'h': The height of the wall, representing how many rows it extends downward
            #  from the 'y' coordinate.
            for i in range(h):
                for j in range(w):
                    # assigning 'X' as walls after the iteration
                    self.grid[y + i][x + j] = 'X'

    # check if a particular cell is free (not a wall) and within grid boundaries
    def is_free(self, x, y):
        if 0 <= y < self.rows and 0 <= x < self.cols and self.grid[y][x] != 'X':
            return True
        return False
