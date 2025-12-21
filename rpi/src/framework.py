pin_layout=[[39, "", "Ground", ""], [37, 26, 1, "y"], [7, 4, 2, "y"], [31, 6, 3, "y"], [23, 11, 4, "y"], [15, 22, 5, "y"], [19, 10, 6, "y"], [5, "", "Ground", "y"], [36, 16, 7, "y"], [18, 24, 8, "y"], [28, 1, 9, "y"], [16, 23, 10, "y"], [22, 25, 11, "y"], [12, 18, 12, "y"]]
import RPi.GPIO as GPIO
import time
from functools import cache

GPIO.setmode(GPIO.BCM)

@cache
def setup_pin(pin):
    GPIO.setup(pin, GPIO.OUT)

pinmap = {wire_num: bcm for _, bcm, wire_num, __ in pin_layout if isinstance(wire_num, int) and bool(bcm)}
def toggle(wire, on=True):
    pin = pinmap[wire]
    setup_pin(pin)
    GPIO.output(pin, on)

def all_off(pins):
    """Turn off all pins"""
    for pin in pins:
        toggle(pin, False)


def apply_pattern(pattern_generator):
    """
    Apply patterns from a generator using the toggle function.

    Usage:
        pattern_gen = heartbeat_pattern()
        apply_pattern(pattern_gen)

    Args:
        pattern_generator: Generator yielding (pattern_string, delay_ms) tuples
    """
    for pattern_string, delay_ms in pattern_generator:
        # Parse the pattern string, extracting only 0s and 1s
        digits = ''.join(c for c in pattern_string if c in '01')

        # Clear all lights first
        for i in range(1, 13):
            toggle(i, False)

        # First 6 digits are top LEDs (1-6)
        # Next 6 digits are bottom LEDs (7-12)
        for i, digit in enumerate(digits[:12]):
            if digit == '1':
                light_number = i + 1
                toggle(light_number, True)

        # Wait for the specified delay
        time.sleep(delay_ms / 1000.0)
