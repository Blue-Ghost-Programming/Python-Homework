# File name: citc1301a03-tpitts-lab11
# Name: T. Josh Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab11
# Due Date: February 17th, 2020
# Description: In this Lab, I learned how to write a Python program that calculates Celsius and Kelvin from Fahrenheit.
import math

def main():

    f = float(input('enter temperature in Fahrenheit '))
    c = (5 / 9) * (f - 32)
    k = (c + 273.15)
    print('Temperature Fahrenheit:', f)
    print('temperature in Celsius:', c)
    print('Temperature in kelvin:', k)

main()