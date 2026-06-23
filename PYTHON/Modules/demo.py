# Inbuilt Modules 

# 1st Syntax 
# The Python math module is a built-in library that gives you access to a wide range of 
# essential mathematical functions and constants. Because it is a core part of Python, 
# you do not need to install it separately; you simply type import math 
# at the top of your script to start using it

# print(math.sqrt(16)) # NameError: name 'math' is not defined. Did you forget to import 'math'?
import math
print(math.sqrt(16))
print(math.pi)

print("=" * 50)

# 2nd Syntax - Recommended
# from module import specific_functionality 
from math import pi
print(pi)

from math import pi,sqrt,e
print(pi)
print(sqrt(16))
print(e)










