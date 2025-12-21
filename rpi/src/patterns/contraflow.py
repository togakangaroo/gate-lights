def contraflow_pattern():
    """
    Contraflow pattern - opposing flows.
    """
    patterns = [
        ("""011111
            111110""", 150),
        ("""101111
            111101""", 250),
        ("""110111
            111011""", 300),
        ("""111011
            110111""", 300),
        ("""111101
            101111""", 250),
        ("""111110
            011111""", 150),
    ]

    while True:
        for p in patterns:
            yield p
        for p in reversed(patterns):
            yield p
