def waterfall_pattern():
    """
    Waterfall pattern - cascade from left to right, top to bottom.
    """
    while True:
        yield ("""100000
                  000000""", 200)
        yield ("""110000
                  100000""", 200)
        yield ("""111000
                  110000""", 200)
        yield ("""111100
                  111000""", 200)
        yield ("""111110
                  111100""", 200)
        yield ("""111111
                  111110""", 200)
        yield ("""011111
                  111111""", 200)
        yield ("""001111
                  011111""", 200)
        yield ("""000111
                  001111""", 200)
        yield ("""000011
                  000111""", 200)
        yield ("""000001
                  000011""", 200)
        yield ("""000000
                  000001""", 200)
        yield ("""000000
                  000000""", 200)
