"""
LED Pattern modules for gate lights.

Each pattern is a generator function that yields (pattern_string, delay_ms) tuples.
Pattern strings contain two rows of 6 binary digits:
- First row: top LEDs (lights 1-6)
- Second row: bottom LEDs (lights 7-12)
"""

from .heartbeat import heartbeat_pattern
from .snake import snake_pattern
from .random_pattern import random_pattern
from .wave import wave_pattern
from .sparkle import sparkle_pattern
from .swizzle import swizzle_pattern
from .mila import mila_pattern
from .gravity import gravity_pattern
from .octopus_isaac import octopus_isaac_pattern
from .contraflow import contraflow_pattern
from .waterfall import waterfall_pattern
from .breathing import breathing_pattern
from .rule30 import rule30_pattern
from .variable_rule30 import variable_rule30_pattern
from .thunder import thunder_pattern
from .explosion import explosion_pattern
from .mushroom_cloud import mushroom_cloud_pattern
from .intensity_wave import intensity_wave_pattern
from .campfire import campfire_pattern
from .shimmer import shimmer_pattern
from .langtons_ant import langtons_ant_pattern
from .inverted_ant import inverted_ant_pattern

__all__ = [
    'heartbeat_pattern',
    'snake_pattern',
    'random_pattern',
    'wave_pattern',
    'sparkle_pattern',
    'swizzle_pattern',
    'mila_pattern',
    'gravity_pattern',
    'octopus_isaac_pattern',
    'contraflow_pattern',
    'waterfall_pattern',
    'breathing_pattern',
    'rule30_pattern',
    'variable_rule30_pattern',
    'thunder_pattern',
    'explosion_pattern',
    'mushroom_cloud_pattern',
    'intensity_wave_pattern',
    'campfire_pattern',
    'shimmer_pattern',
    'langtons_ant_pattern',
    'inverted_ant_pattern',
]
