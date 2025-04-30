import math
from decimal import Decimal, getcontext

# The McLaurin Series for arctan(x) is:
# x - x^3/3 + x^5/5 - x^7/7 + x^9/9 - x^11/11 + ...
# \sum_{i = 1}^{n_iter} (-1)^(i) x^(2i + 1)/(2i + 1)

# tan(45) = tan(pi/4) = 1
# So, arctan(1) = pi/4
# We can approximate arctan(1) * 4 to get our pi approximation

# The Mclaurin Series for arctan(1) is:
# \sum_{i = 1}^{n_iter} (-1)^(i)/(2i + 1)


def gregory_series(n_iter, n_places):
    getcontext().prec = n_places

    result = Decimal(0)
    numerator = Decimal(1)

    for i in range(1, n_iter * 2 + 1, 2):
        result += numerator / i
        numerator *= -1

    return Decimal(4) * result


n_iter = 10**7

n_places = 2000
pi_approx = gregory_series(n_iter, n_places)

print(f"Gregory Series Pi Approximation: {pi_approx}")
print("\n\n")
print(f"Absolute Error: {abs(pi_approx - Decimal(math.pi))}")
print("\n\n")
