# Filename: citc1301a03-tpitts-lab16
# Name: Timothy J Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: lab16
# Due Date: 2/26/2020
# Description: making an upside down pyramid with nested for loops.
import math

def main():

    count = 9
    for x in range(count):
        for j in range(x):
            print(f' ', end='')
        for y in range(count-2*x):
            print(f'X',end='')
        print()

main()
