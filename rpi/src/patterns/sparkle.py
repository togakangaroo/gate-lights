import random


def sparkle_pattern():
    """
    Sparkle pattern - creates 1-3 random sparkles.
    """
    while True:
        # Create 1-3 random sparkles
        num_sparkles = random.randint(1, 3)
        all_positions = list(range(12))

        # Shuffle
        random.shuffle(all_positions)

        top_row = ['0'] * 6
        bottom_row = ['0'] * 6

        for i in range(num_sparkles):
            pos = all_positions[i]
            if pos < 6:
                top_row[pos] = '1'
            else:
                bottom_row[pos - 6] = '1'

        yield (f"""{''.join(top_row)}
                   {''.join(bottom_row)}""", 300)
