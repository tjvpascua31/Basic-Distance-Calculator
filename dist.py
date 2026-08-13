# by Trosindel John V. Pascua in 8 - Molave

import math

# Input wrapper to catch non-floats
def input_wrapper(s):
    while True:
        try:
            result = float(input(s))
            break
        except ValueError:
            print("Invalid value, try again.")
    return result

# globals() trick (check https://www.geeksforgeeks.org/python/python-globals-function/)
for name in ["x1","y1","x2","y2"]:
    globals()[name] = input_wrapper(f"Enter {name}: ")

# Highlighter might say x1,x2,etc. isn't defined,
# This is fine
dist = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

# Print distance to 3 decimal points
print("\nThe Distance between two points is:", f"{dist:.3f}")

# For running in cmd.exe
input("Press enter to terminate")

"""
Reflection:

pow() and math.sqrt() were helpful in this program because I don't have to implement square rooting or exponents anymore.
The algorithm for square roots is very interesting but it's not useful when I am trying to do work.
"""