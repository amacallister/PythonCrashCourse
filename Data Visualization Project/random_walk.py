from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, direction_range, steps):
        """Determine the direction and distance for each step, and calculate the next step."""

        direction = choice(direction_range)
        distance = choice(steps)
        step = direction * distance
        return step
    
    def fill_walk(self, x_direction_range=[1, -1], y_direction_range=[1, -1], x_steps=[0, 1, 2, 3, 4,], y_steps=[0, 1, 2, 3, 4,]):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_step = self.get_step(x_direction_range, x_steps)
            y_step = self.get_step(y_direction_range, y_steps)

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    
        