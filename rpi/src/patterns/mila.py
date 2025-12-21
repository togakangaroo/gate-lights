def mila_pattern():
    """
    Mila pattern - specific blink pattern.
    """
    while True:
        yield ("""100100
                  000010""", 600)
        for _ in range(3):
            yield ("""111111
                      111111""", 400)
            yield ("""000000
                      000000""", 400)
