def snake_pattern():
    """
    Snake pattern generator that yields (pattern, delay_ms) tuples.
    Creates a snake-like movement across the rods.
    Pattern format: Two rows of 6 binary digits each
    - First row: top LEDs (lights 1-6)
    - Second row: bottom LEDs (lights 7-12)
    """
    while True:
        yield ("""111100
                  000100""", 500)
        yield ("""011110
                  000010""", 500)
        yield ("""001111
                  000001""", 500)
        yield ("""000111
                  000001""", 500)
        yield ("""000011
                  000011""", 500)
        yield ("""000101
                  000111""", 500)
        yield ("""001000
                  001111""", 500)
        yield ("""010000
                  011110""", 500)
        yield ("""100000
                  111100""", 500)
        yield ("""100000
                  111000""", 500)
        yield ("""110000
                  110000""", 500)
        yield ("""111000
                  101000""", 500)
