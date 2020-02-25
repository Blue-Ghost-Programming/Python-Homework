# Filename: CITC1301A03-tpitts-Lab15
# Name: timothy pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab15
# Due Date: February 26th, 2020
# Description: In this lab, I learned how to use math to find the area, and circumference, and radius of a circle using
# range and for loop.

from math import pi

def main():

    radius = int(input('input radius of a circle greater than 5cm: '))
    print('radius       area        circumference')
    for x in range(5, radius+1):
        area = pi * (radius*radius)
        circumference = pi * (2*radius)
        print(f' {x:2d} {area:13.2f} {circumference: 15.2f}')

main()