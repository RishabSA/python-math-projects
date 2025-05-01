import numpy as np
import math

# The Monte Carlo Approximation of π involves random numbers
# We generate random numbers for the x and y falling within [-1, 1] on the x and y axes
# We then find the number of those points that fall within a circle with a radius of 1 inside of the square
# We find the ratio of points in the circle to the number of total points and multiply by 4 to get the π approximation


def monte_carlo(n_points: int):
    x_points = np.random.rand(n_points) * 2.0 - 1.0
    y_points = np.random.rand(n_points) * 2.0 - 1.0

    n_in = len(
        np.array(
            [i for i in range(n_points) if (x_points[i] ** 2 + y_points[i] ** 2 < 1.0)]
        )
    )

    pi_approx = 4.0 * (n_in / n_points)
    return pi_approx


n_points = 10**7
pi_approx = monte_carlo(n_points)

print(f"Monte Carlo Pi Approximation: {pi_approx}")
print("\n\n")
print(f"Absolute Error: {abs(pi_approx - math.pi)}")
print("\n\n")
