# File name: citc1301a03-tpitts-lab10
# Name: T. Josh Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab10
# Due Date: February 17th, 2020
# Description: in this lab I learned to use python to do basic trigonometry.
import math

def main():

    x = 0
    y = 90
    z = -45

    print('x = 0')
    print('y = 90')
    print('z = -45')

    sine = math.sin(x)
    cosine = math.cos(x)
    tangent = math.tan(x)
    ar = math.radians(x)
    print(f'angle of x in radians  = {ar}')
    print(f'Sine of x = {sine}')
    print(f'Cosine of x = {cosine}')
    print(f'Tangent of x = {tangent}')

    sine = math.sin(y)
    cosine = math.cos(y)
    tangent = math.tan(y)
    ar = math.radians(y)
    print(f'angle of y in radians = {ar}')
    print(f'Sine of y = {sine}')
    print(f'Cosine of y = {cosine}')
    print(f'Tangent of y = {tangent}')

    sine = math.sin(z)
    cosine = math.cos(z)
    tangent = math.tan(z)
    ar = math.radians(z)
    print(f'angle of z in radians = {ar}')
    print(f'Sine of z = {sine}')
    print(f'Cosine of z = {cosine}')
    print(f'Tangent of z = {tangent}')

main()