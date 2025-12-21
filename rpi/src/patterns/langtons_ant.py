import random


def langtons_ant_pattern():
    """
    Langton's Ant - Simple rules create complex emergent behavior.
    Ant turns left on 1, right on 0, and flips the cell.
    Simulates on larger 6x12 grid, displays 2x6 window following the ant.
    """
    GRID_ROWS = 6
    GRID_COLS = 12
    DISPLAY_ROWS = 2
    DISPLAY_COLS = 6

    grid = [[0] * GRID_COLS for _ in range(GRID_ROWS)]

    ant_row = random.randint(0, GRID_ROWS - 1)
    ant_col = random.randint(0, GRID_COLS - 1)
    ant_dir = random.randint(0, 3)  # 0=up, 1=right, 2=down, 3=left

    while True:
        # Calculate display window centered on ant
        display_start_row = max(0, min(GRID_ROWS - DISPLAY_ROWS, ant_row - DISPLAY_ROWS // 2))
        display_start_col = max(0, min(GRID_COLS - DISPLAY_COLS, ant_col - DISPLAY_COLS // 2))

        # Extract 2x6 window
        display_grid = []
        for r in range(DISPLAY_ROWS):
            display_grid.append([])
            for c in range(DISPLAY_COLS):
                display_grid[r].append(grid[display_start_row + r][display_start_col + c])

        # Show ant position if it's in the display window
        ant_display_row = ant_row - display_start_row
        ant_display_col = ant_col - display_start_col
        if (0 <= ant_display_row < DISPLAY_ROWS and
                0 <= ant_display_col < DISPLAY_COLS):
            display_grid[ant_display_row][ant_display_col] = 1

        top_str = ''.join(str(x) for x in display_grid[0])
        bottom_str = ''.join(str(x) for x in display_grid[1])
        yield (f"""{top_str}
                   {bottom_str}""", 250)

        # Apply Langton's Ant rules
        current_cell = grid[ant_row][ant_col]

        if current_cell == 0:
            # Turn right (clockwise)
            ant_dir = (ant_dir + 1) % 4
        else:
            # Turn left (counter-clockwise)
            ant_dir = (ant_dir + 3) % 4

        # Flip current cell
        grid[ant_row][ant_col] = 1 - current_cell

        # Move forward with wrapping on larger grid
        if ant_dir == 0:
            ant_row = (ant_row - 1) % GRID_ROWS      # up
        elif ant_dir == 1:
            ant_col = (ant_col + 1) % GRID_COLS      # right
        elif ant_dir == 2:
            ant_row = (ant_row + 1) % GRID_ROWS      # down
        elif ant_dir == 3:
            ant_col = (ant_col - 1) % GRID_COLS      # left
