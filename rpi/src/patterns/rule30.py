import random


def rule30_pattern():
    """
    Rule 30 - Elementary Cellular Automaton.
    Famous for producing complex, chaotic patterns from simple rules.
    """
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0]  # Start with single cell in middle
    ]

    last_state = None

    while True:
        # Convert grid to string
        top_str = ''.join(str(x) for x in grid[0])
        bottom_str = ''.join(str(x) for x in grid[1])
        current_state = f"{top_str}{bottom_str}"

        yield (f"""{top_str}
                   {bottom_str}""", 400)

        # Evolve bottom row according to Rule 30
        new_bottom = []
        for i in range(6):
            left = grid[1][(i - 1) % 6]   # Wrap around
            center = grid[1][i]
            right = grid[1][(i + 1) % 6]  # Wrap around

            # Rule 30: 111->0, 110->0, 101->0, 100->1, 011->1, 010->1, 001->1, 000->0
            pattern = (left << 2) | (center << 1) | right
            new_val = (30 >> pattern) & 1
            new_bottom.append(new_val)

        # Shift: top becomes old bottom, bottom becomes new generation
        grid[0] = grid[1][:]
        grid[1] = new_bottom

        # Reset if pattern is stuck (same as last step)
        new_state = f"{''.join(str(x) for x in grid[0])}{''.join(str(x) for x in grid[1])}"
        if new_state == last_state:
            # Yield the stuck state once
            yield (f"""{''.join(str(x) for x in grid[0])}
                       {''.join(str(x) for x in grid[1])}""", 400)

            # Reset with random starting position
            new_grid = [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]
            ]

            # Turn on 1-3 random cells in bottom row
            num_cells = random.randint(1, 3)
            for i in range(num_cells):
                random_col = random.randint(0, 5)
                new_grid[1][random_col] = 1

            grid = new_grid
            last_state = None
        else:
            last_state = current_state
