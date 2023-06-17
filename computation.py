import os
import math

import numpy as np

import Area as ar # as keyword is alias
from Perimeter import circle, rectangle #from keyword to import specific function(s)

print("Area of a circle is {}".format(ar.circle(10))) # string format

print(f"Area is {ar.circle(10)}") # f string

print ("Area is %d" %(ar.circle(10))) # older format


print (f"perimeter of a circle is {circle(10)}")