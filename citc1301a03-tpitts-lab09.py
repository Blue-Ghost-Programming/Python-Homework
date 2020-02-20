# File name: citc1301a03-tpitts-lab09
# Name: T. Josh Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab09
# Due Date: February 13th, 2020
# Description: In this lab I learned to print absolute, rounded, ceiling, and floor
# values of each variable.
import math
def main():

    x = 4.54
    y = 6.29
    z = -4.71
    i = 3
    j = -5

    print('absolute value of x =', abs(x))
    print('absolute value of y =', abs(y))
    print('absolute value of z =', abs(z))
    print('absolute value of i =', abs(i))
    print('absolute value of j =', abs(j))

    print('rounded value of x =', round(x, 1))
    print('rounded value of y =', round(y, 1))
    print('rounded value of z =', round(z, 1))
    print('rounded value of i =', round(i, 1))
    print('rounded value of j =', round(j, 1))

    print("ceiling value of x =", math.ceil(x))
    print("ceiling value of y =", math.ceil(y))
    print("ceiling value of z =", math.ceil(z))
    print("ceiling value of i =", math.ceil(i))
    print("ceiling value of j =", math.ceil(j))

    print("floor value of x =", math.floor(x))
    print("floor value of y =", math.floor(y))
    print("floor value of z =", math.floor(z))
    print("floor value of i =", math.floor(i))
    print("floor value of j =", math.floor(j))

main()