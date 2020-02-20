# File name: citc1301a03-tpitts-lab05
# Name: T. Josh Pitts
# Username: tpitts
# Course and Section: CITC 1301 A03
# Assignment: Lab05
# Due Date: February 5th, 2020
# Description: In this lab I learned how to write a program that would output the answers to basic math problems with-
# -numbers entered by the user.

int1 = int(input('enter the 1st integer '))
int2 = int(input('enter the 2nd integer '))
flt1 = float(input('enter the 1st floating point number '))
flt2 = float(input('enter the 2nd floating point number '))

print('ineger 1:', int1)
print('1st integer type:', type(int1))
print('ineger 2:', int2)
print('2nd integer type:', type(int2))
print('Floating number 1:', flt1)
print('1st floating number type:', type(flt1))
print('Floating number 2:', flt2)
print('2nd floating number type:', type(flt2))

print('integer 1 / integer 2 =', int1/int2)
print('intger1 x integer 2 =', int1*int2)
print('float 1 / float 2 =', flt1/flt2)
print('float1 x float 2=', flt1*flt2)
print('data type of float 1 / float 2:', type(flt1/flt2))
print('integer1 / float 2=', int1/flt2)
print('data type of integer 1 / float 2:', type(int1/flt2))
print('float 1 x integer 1=', flt1*int1)
print('data type of float 1 / integer 1:', type(flt1/int1))
