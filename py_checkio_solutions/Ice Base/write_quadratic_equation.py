#!/usr/local/bin/checkio --domain=py run write-quadratic-equation

# Quadratic Equationmay be expressed as a product
# a(x-x1)(x-x2) = 0,
# where x1 and x2 are the solutions of equation, so called roots.    After opening the brackets you receive well known form
# a*x**2 + b*x + c = 0.
# This is what you should do in this mission. You have input list with    integers - a, x1 [, x2]. If it has length 2, it means, x1 == x2: equation    has two equal roots (one distinct root). You function should return quadratic equation as a string.    Pay attention to specific cases. UseQuadratic Formula Calculatorfor recheck. Good luck!
# 
# Input:List with 2-3 integers.
# 
# Output:String.
# 
# Examples:
# 
# assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
# assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
# assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
# assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"Precondition:a != 0; abs(a) == 1 -> '[-]x**2'; a != abs(1) - > '[-]a*x**2'
# exactly one whitespace around signs: [-]a*x**2 sign b*x sign c = 0
# abs(b) == 1 -> [-]a*x**2 sign x sign c = 0
# keep correct view and spacing when x1=x2=0, x1 or x2 = 0, x1=-x2
# 
# 
# END_DESC

def quadr_equation(data: list[int]) -> str:
    # your code here
    return ""


print("Example:")
print(quadr_equation([2, 4, 6]))

assert quadr_equation([2, 4, 6]) == "2*x**2 - 20*x + 48 = 0"
assert quadr_equation([-2, 4, 6]) == "-2*x**2 + 20*x - 48 = 0"
assert quadr_equation([2, 4, -4]) == "2*x**2 - 32 = 0"
assert quadr_equation([2, 4, 0]) == "2*x**2 - 8*x = 0"
assert quadr_equation([2, 0]) == "2*x**2 = 0"
assert quadr_equation([2, 4]) == "2*x**2 - 16*x + 32 = 0"

print("The mission is done! Click 'Check Solution' to earn rewards!")