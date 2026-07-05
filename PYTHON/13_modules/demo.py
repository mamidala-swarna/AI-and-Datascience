# print(math.sqrt(16)) # NameError: name 'math' is not defined. Did you forget to import 'math'?

import math
print(math.sqrt(16))
print(math.pi)

print("=" * 50)

# 2nd Syntax - Recommended
# from module import specific_functionality 
from math import pi 
print(pi)
# print(sqrt(16)) # NameError: name 'sqrt' is not defined

from math import pi,sqrt,e  
print(pi)
print(sqrt(16)) 
print(e)
