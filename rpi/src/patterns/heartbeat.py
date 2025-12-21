def heartbeat_pattern():
    """
    Heartbeat pattern generator that yields (pattern, delay_ms) tuples.
    Pattern format: Two rows of 6 binary digits each
    - First row: top LEDs (lights 1-6)
    - Second row: bottom LEDs (lights 7-12)
    """
    while True:
        # First beat (systole) - quick flash from center outward
        yield (""" 000000
                   001100""", 100)
        yield (""" 001100
                   011110""", 100)
        yield (""" 011110
                   111111""", 150)

        # Brief pause
        yield (""" 000000
                   000000""", 100)

        # Second beat (diastole) - slightly weaker
        yield (""" 000000
                   001100""", 100)
        yield (""" 001100
                   011110""", 150)

        # Longer pause before next heartbeat
        yield (""" 000000
                   000000""", 600)
