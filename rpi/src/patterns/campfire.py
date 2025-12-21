import random


def campfire_pattern():
    """
    Campfire - Random flickering at different intensity levels.
    """
    rod_states = [0, 0, 0, 0, 0, 0]  # 0=off, 1=half, 2=full

    while True:
        # Update each rod randomly
        for i in range(6):
            rand = random.random()
            if rand < 0.3:
                rod_states[i] = max(0, rod_states[i] - 1)  # Dim
            elif rand < 0.6:
                rod_states[i] = min(2, rod_states[i] + 1)  # Brighten
            # else stay the same

        # Convert rod states to LED pattern
        top_row = ''.join('1' if s == 2 else '0' for s in rod_states)
        bottom_row = ''.join('1' if s >= 1 else '0' for s in rod_states)

        yield (f"""{top_row}
                   {bottom_row}""", 150)
