# using import statement to import a module

# Packages gives us access to pre-built functions

import sys
import math
import os

# Importing specific functions from a module
from math import pi


print('Python version:',sys.version) # To get python version
print('Square root of a given number:',math.sqrt(4))
print('PI value:',math.pi)
print('PI value without module name:',pi)

# os.name: This function gives the name of the operating system.
print('OS name:',os.name)
# os.getcwd: This function returns the current working directory.
print(os.getcwd())
# os.listdir: This function returns a list of all files and directories in the specified directory.
print('List directory:',os.listdir())

# os.mkdir: This function creates a new directory.
# os.remove: This function removes or deletes a file.
# os.rename: This function renames a file or directory.
# os.environ: This function returns a dictionary of the user’s environment variables.

# print('Environmental variables:',os.environ)

print('System Path:',sys.path)

for path in sys.path:
    print(path)

print(sys.modules)