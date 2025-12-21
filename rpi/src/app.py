# /// script
# dependencies = [
#   "RPi.GPIO",
# ]
# ///

import sys
from framework import apply_pattern
from patterns import (
    heartbeat_pattern,
    snake_pattern,
    random_pattern,
    wave_pattern,
    sparkle_pattern,
    swizzle_pattern,
    mila_pattern,
    gravity_pattern,
    octopus_isaac_pattern,
    contraflow_pattern,
    waterfall_pattern,
    breathing_pattern,
    rule30_pattern,
    variable_rule30_pattern,
    thunder_pattern,
    explosion_pattern,
    mushroom_cloud_pattern,
    intensity_wave_pattern,
    campfire_pattern,
    shimmer_pattern,
    langtons_ant_pattern,
    inverted_ant_pattern,
)

# Map pattern names to pattern functions
PATTERNS = {
    'heartbeat': heartbeat_pattern,
    'snake': snake_pattern,
    'random': random_pattern,
    'wave': wave_pattern,
    'sparkle': sparkle_pattern,
    'swizzle': swizzle_pattern,
    'mila': mila_pattern,
    'gravity': gravity_pattern,
    'octopus_isaac': octopus_isaac_pattern,
    'contraflow': contraflow_pattern,
    'waterfall': waterfall_pattern,
    'breathing': breathing_pattern,
    'rule30': rule30_pattern,
    'variable_rule30': variable_rule30_pattern,
    'thunder': thunder_pattern,
    'explosion': explosion_pattern,
    'mushroom_cloud': mushroom_cloud_pattern,
    'intensity_wave': intensity_wave_pattern,
    'campfire': campfire_pattern,
    'shimmer': shimmer_pattern,
    'langtons_ant': langtons_ant_pattern,
    'inverted_ant': inverted_ant_pattern,
}


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run app.py <pattern_name>")
        print("\nAvailable patterns:")
        for name in sorted(PATTERNS.keys()):
            print(f"  - {name}")
        sys.exit(1)

    pattern_name = sys.argv[1]

    if pattern_name not in PATTERNS:
        print(f"Error: Unknown pattern '{pattern_name}'")
        print("\nAvailable patterns:")
        for name in sorted(PATTERNS.keys()):
            print(f"  - {name}")
        sys.exit(1)

    pattern_func = PATTERNS[pattern_name]
    apply_pattern(pattern_func())


if __name__ == '__main__':
    main()
