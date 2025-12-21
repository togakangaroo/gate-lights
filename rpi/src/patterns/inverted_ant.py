from .langtons_ant import langtons_ant_pattern


def inverted_ant_pattern():
    """
    Inverted Langton's Ant - Rules reversed: turn left on 0, right on 1.
    """
    ant = langtons_ant_pattern()
    for pattern, delay in ant:
        # Invert 0s and 1s
        inverted = pattern.replace('0', 'p').replace('1', '0').replace('p', '1')
        yield (inverted, delay)
