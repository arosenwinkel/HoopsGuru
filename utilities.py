# utilities.py

# various functions that are used throughout the game

import random


def weighted_choice(choices):  # takes in a dictionary as an argument
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    limit = 0
    for c, w in choices.items():
        if limit + w > r:
            return c
        limit += w


def height_to_feet(height):  # convert height in inches into the normal way of displaying it, e.g. 6'7"
    feet = int(height / 12)
    inches = height % 12
    return '''{}'{}"'''.format(feet, inches)
