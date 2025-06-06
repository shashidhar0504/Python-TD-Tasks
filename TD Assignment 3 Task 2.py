#Using the Math Module for Calculations
'''Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
'''

import math
n = int(input("Enter a Number : "))
sqrt_value =print("Square root of ",n ,"is ", math.sqrt(n))
nlog_value =print("Natural logarithm of ",n," is ", math.log(n))
sine_valie =print("Sine of the number ",n," is ", math.sin(n))