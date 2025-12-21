def swizzle_pattern():
    """
    Swizzle pattern - rotating pattern.
    """
    while True:
        yield ("""110111
                  011101""", 300)
        yield ("""111011
                  101110""", 300)
        yield ("""111101
                  010111""", 300)
        yield ("""111110
                  101011""", 300)
        yield ("""011111
                  110101""", 300)
        yield ("""101111
                  111010""", 300)
