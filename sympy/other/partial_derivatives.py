import sympy as sp

# Find the partial derivative of f(x, y) = x^2 * y + y^3 with respect to x and the partial derivative with respect to y

x = sp.symbols("x")
y = sp.symbols("y")
f = x**2 * y + y**3


def calculate_partial_derivative(function, variable):
    derivative_x = sp.diff(function, variable)
    return derivative_x


partial_derivative_wrt_x = calculate_partial_derivative(f, x)
print(
    f"The partial derivative of the function with respect to x is: {partial_derivative_wrt_x}"
)

partial_derivative_wrt_y = calculate_partial_derivative(f, y)
print(
    f"The partial derivative of the function with respect to y is: {partial_derivative_wrt_y}"
)
