# Filename: CITC1301A03-tpitts-Lab14
# Name: tpitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab14
# Due Date: February 26th, 2020
# Description: In this lab I learned how to use for loops and the range command.
import math

def main():
   total = 0
   count = int(input('enter a start number: '))
   numb = int(input('Enter a end number: '))
   for x in range(count, numb+1):
        total += x

   print(f'Total = {total}')

main()
