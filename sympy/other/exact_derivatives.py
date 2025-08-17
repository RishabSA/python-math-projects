import sympy as sp

# Find the exact derivative of f(x) = cos(x) for x = pi/3

x = sp.symbols("x")
x_val = sp.pi / 3
f = sp.cos(x)


def calculate_exact_derivative(function, variable, value):
    f_derivative = sp.diff(function, variable)
    derivative_val = f_derivative.subs(variable, value).simplify()
    return derivative_val


exact_derivative = calculate_exact_derivative(f, x, x_val)
print(
    f"The exact derivative of the function with respect to x at pi/3 is: {exact_derivative}"
)
