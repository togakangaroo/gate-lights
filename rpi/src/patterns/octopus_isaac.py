def octopus_isaac_pattern():
    """
    Octopus Isaac pattern.
    """
    while True:
        yield ("""101110
                  011101""", 300)
        yield ("""011111
                  111110""", 300)
        yield ("""111111
                  111111""", 300)
        yield ("""000000
                  000000""", 300)
        yield ("""111110
                  011111""", 300)
        yield ("""011101
                  101110""", 300)
