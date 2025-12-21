def wave_pattern():
    """
    Wave pattern - lights move right then left.
    """
    while True:
        # Moving right
        yield ("""100000
                  110000""", 100)
        yield ("""010000
                  111000""", 100)
        yield ("""001000
                  111100""", 100)
        yield ("""000100
                  011110""", 100)
        yield ("""000010
                  001111""", 100)
        yield ("""000001
                  000111""", 100)
        yield ("""000001
                  000011""", 100)
        # Moving left
        yield ("""000010
                  000111""", 100)
        yield ("""000100
                  001111""", 100)
        yield ("""001000
                  011110""", 100)
        yield ("""010000
                  111100""", 100)
        yield ("""100000
                  111000""", 100)
