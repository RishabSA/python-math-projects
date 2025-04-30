import math
from decimal import Decimal, getcontext


def archimedes(n_iter, n_places):
    getcontext().prec = n_places

    polygon_edge_length_squared = Decimal(2)
    polygon_sides = 2

    for i in range(n_iter):
        polygon_edge_length_squared = (
            2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt()
        )
        polygon_sides *= 2

    return polygon_sides * polygon_edge_length_squared.sqrt()


n_iter = 1000

n_places = 2000
pi_approx = archimedes(n_iter, n_places)

print(f"Archimedes Pi Approximation: {pi_approx}")
print("\n\n")
print(f"Absolute Error: {abs(pi_approx - Decimal(math.pi))}")
print("\n\n")
