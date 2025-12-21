def mushroom_cloud_pattern():
    """
    Mushroom Cloud - Nuclear explosion forming a mushroom cloud.
    """
    while True:
        # Initial ground burst
        yield ("""000000
                  001100""", 100)

        # Fireball rises
        yield ("""001100
                  011110""", 100)

        yield ("""011110
                  111111""", 80)

        # Flash at detonation
        yield ("""111111
                  111111""", 60)

        # Mushroom cap forms at top
        yield ("""111111
                  011110""", 150)

        yield ("""111111
                  001100""", 150)

        # Cap expands, stem becomes visible
        yield ("""111111
                  001100""", 200)

        # Classic mushroom shape - wide cap, narrow stem
        yield ("""111111
                  001100""", 250)

        # Cap starts to dissipate
        yield ("""011110
                  001100""", 300)

        yield ("""001100
                  000000""", 400)

        # Fade to darkness
        yield ("""000000
                  000000""", 500)

        # Long pause before next detonation
        yield ("""000000
                  000000""", 1500)
