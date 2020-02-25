#File name: citc1301a03-tpitts-lab13
# Name: T. Josh Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab13
# Due Date: February 26th, 2020
# Description: In this lab I learned of to use a loop and the range command.

import math

def main():
    i = int
    N = int(input('Upper limit: '))
    print('upper limit =', N)
    print('odd numbers from 1 to', N,':')
    for x in range(1, N + 1):
        if (x % 2 != 0):
            print("{0}".format(x))

main()