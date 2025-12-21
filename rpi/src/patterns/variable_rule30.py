from .rule30 import rule30_pattern


def variable_rule30_pattern():
    """
    Rule 30 with variable timing based on number of lit cells.
    """
    rule30_gen = rule30_pattern()

    for pattern, _ in rule30_gen:
        lines = pattern.split('\n')
        # Count '1's in each line
        count_1_line0 = lines[0].strip().count('1')
        count_1_line1 = lines[1].strip().count('1')

        timing = 100 * (count_1_line1 - count_1_line0)
        timing = max(0, timing)
        timing += 200

        yield (pattern, timing)
