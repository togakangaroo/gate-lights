import random


def gravity_pattern():
    """
    Gravity pattern - lights fall down like gravity.
    """
    # Track state for each rod: -1 = off, 0+ = timesteps since lit
    rod_states = [-1, -1, -1, -1, -1, -1]

    # Weights for each rod (bell curve - center rods 2x more likely than edges)
    weights = [1, 1.5, 2, 2, 1.5, 1]
    total_weight = sum(weights)

    while True:
        # Select a random rod to light up (weighted)
        rand = random.random() * total_weight
        cumulative = 0
        selected_rod = 0
        for i in range(6):
            cumulative += weights[i]
            if rand <= cumulative:
                selected_rod = i
                break

        # Light up the selected rod
        rod_states[selected_rod] = 0

        # Build pattern based on current states
        top_row = []
        bottom_row = []

        for i in range(6):
            if rod_states[i] == -1 or rod_states[i] >= 4:
                # Rod is off
                top_row.append('0')
                bottom_row.append('0')
            elif rod_states[i] < 2:
                # Rod is fully lit (timesteps 0-1)
                top_row.append('1')
                bottom_row.append('1')
            else:
                # Only bottom lit (timesteps 2-3) - gravity pulls light down
                top_row.append('0')
                bottom_row.append('1')

        yield (f"""{''.join(top_row)}
                   {''.join(bottom_row)}""", 400)

        # Increment all active rod states
        for i in range(6):
            if rod_states[i] >= 0:
                rod_states[i] += 1
                if rod_states[i] >= 4:
                    rod_states[i] = -1  # Turn off
