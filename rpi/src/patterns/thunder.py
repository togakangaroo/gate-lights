import random


def thunder_pattern():
    """
    Thunder - Random lightning flashes with variable delays simulating a storm.
    """
    while True:
        # Lightning flash - full brightness
        yield ("""111111
                  111111""", 80)

        # Quick second flash (sometimes lightning strikes twice)
        if random.random() < 0.3:
            yield ("""000000
                      000000""", 50)
            yield ("""111111
                      111111""", 80)

        # Darkness
        yield ("""000000
                  000000""", 200)

        # Variable pause before next strike (1-4 seconds)
        pause = 1000 + random.random() * 3000
        yield ("""000000
                  000000""", pause)
