import random


def shimmer_pattern():
    """
    Shimmer - Random rods pulsing independently at different brightness levels.
    """
    rod_states = [0, 0, 0, 0, 0, 0]      # Current brightness: 0=off, 1=half, 2=full
    rod_directions = [1, 1, 1, 1, 1, 1]  # 1=brightening, -1=dimming

    while True:
        # Update each rod independently
        for i in range(6):
            rod_states[i] += rod_directions[i]

            # Reverse direction at boundaries
            if rod_states[i] >= 2:
                rod_states[i] = 2
                rod_directions[i] = -1
            elif rod_states[i] <= 0:
                rod_states[i] = 0
                rod_directions[i] = 1

            # Occasionally change direction randomly for variety
            if random.random() < 0.1:
                rod_directions[i] = 1 if random.random() < 0.5 else -1

        # Convert rod states to LED pattern
        top_row = ''.join('1' if s == 2 else '0' for s in rod_states)
        bottom_row = ''.join('1' if s >= 1 else '0' for s in rod_states)

        yield (f"""{top_row}
                   {bottom_row}""", 200)
