# /// script
# dependencies = [
#   "RPi.GPIO",
# ]
# ///

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

apply_pattern(waterfall_pattern())
