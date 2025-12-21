import random


def random_pattern():
    """
    Random pattern generator - picks random lights each iteration.
    """
    while True:
        # Pick a random number of lights (0-12)
        num_lights = random.randint(0, 12)

        # Create array of all light positions [0-11]
        all_lights = list(range(12))

        # Shuffle using random.shuffle
        random.shuffle(all_lights)

        # Create pattern string
        top_row = ['0'] * 6
        bottom_row = ['0'] * 6

        for i in range(num_lights):
            light_index = all_lights[i]
            if light_index < 6:
                top_row[light_index] = '1'
            else:
                bottom_row[light_index - 6] = '1'

        yield (f"""{''.join(top_row)}
                   {''.join(bottom_row)}""", 1000)
