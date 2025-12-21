def explosion_pattern():
    """
    Explosion - Expands outward from center with accelerating speed.
    """
    while True:
        # Darkness before next explosion
        yield ("""000000
                  000000""", 800)

        # Ignition - center lights up
        yield ("""000000
                  001100""", 150)

        # Rapid expansion
        yield ("""001100
                  011110""", 100)

        yield ("""011110
                  111111""", 80)

        # Full blast
        yield ("""111111
                  111111""", 60)

        # Flash
        yield ("""111111
                  111111""", 40)

        # Fade slowly - dust settling
        yield ("""011110
                  111111""", 200)

        yield ("""001100
                  011110""", 300)

        yield ("""000000
                  011110""", 300)

        yield ("""000000
                  001100""", 400)
