from random import randint

class Die:
    """Generic die class"""

    def __init__(self):
        """Initialize the die class."""
        self.sides = 6

    def roll_die(self):
        """Print a random number between 1 and the number of sides on the die."""
        num = randint(1, self.sides)
        print(num)