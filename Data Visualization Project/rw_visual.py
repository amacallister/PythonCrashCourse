import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:

    # Make a random walk.
    rw = RandomWalk(50_000)
    x_direction_range = [1, -1]
    y_direction_range = [1, -1]
    x_steps = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    y_steps = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    rw.fill_walk(x_direction_range, y_direction_range, x_steps, y_steps)

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Emphasize the first and last points:
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break