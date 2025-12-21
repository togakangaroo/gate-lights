def intensity_wave_pattern():
    """
    Intensity Wave - Brightness wave sweeping across the rods.
    Treats each rod as having 3 brightness levels: off (00), half (01), full (11).
    """
    while True:
        # Wave moving left to right
        yield ("""000000
                  000000""", 200)  # All off

        yield ("""000000
                  100000""", 200)  # Rod 1 half

        yield ("""100000
                  110000""", 200)  # Rod 1 full, Rod 2 half

        yield ("""010000
                  111000""", 200)  # Rod 1 half, Rod 2 full, Rod 3 half

        yield ("""001000
                  011100""", 200)  # Rod 2 half, Rod 3 full, Rod 4 half

        yield ("""000100
                  001110""", 200)  # Rod 3 half, Rod 4 full, Rod 5 half

        yield ("""000010
                  000111""", 200)  # Rod 4 half, Rod 5 full, Rod 6 half

        yield ("""000001
                  000011""", 200)  # Rod 5 half, Rod 6 full

        yield ("""000000
                  000001""", 200)  # Rod 6 half

        yield ("""000000
                  000000""", 200)  # All off
