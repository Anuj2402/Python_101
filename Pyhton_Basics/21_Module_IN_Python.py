'''
module = a file containing a set of functions you want to include in your application.
There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules
use 'import' keyword to import a module(built-in or custom) in python
useful to break down large programs into small manageable and organized files

'''
print(help('modules')) # list of all modules in python

# Example 1
print("Example 1")
import math
# import math as m # alias
# from math import pi
#from math import e # import only e from math module
# print(pi.sqrt(16)) # 4.0
 
a,b,c,d,e = 1,2,3,4,5
print(math.sqrt(a))
print(math.pow(b,c))
print(math.e ** a)
print(math.exp(e))
print(math.e ** e)
print(math.e ** d)
print(math.log(d))


'''
if __name__ == "__main__": is used to execute some code only if the file was run directly, and not imported
function and classes in this module can be resued without the main block of code executing every time
good  precitice ( code is modular , 
                    helps readability,
                    leaves no global variables,
                    avoid unintended execution of code)
)

'''
print(dir); # list of all functions in math module
print(__name__) # __main__