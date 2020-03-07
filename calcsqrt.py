#! /user/bin/env/python3

# Abdalla Fadul
#calculate the square root of number.

def sqrt(x):
    """
    Calculate the square root of argument x.
    """

    # Check that x is positive.
    if x < 0:
        print("Error negative value supplied")
        return -1
    else:
        print("Here we go..")

    # Initial guess for the square root.
    z = x / 2.0

    # Continuously ipmrove the guess.
    # Adapted from https://toor.golang.org/flowcontrol/8
    while abs(x - (z*z)) > 0.01:
        z = z - (((z * z) - x) / (2 * z))

    return z

myval = 63.0
print("The square root of", myval, "is", sqrt(myval))


