# Add standard Python references
#https://github.com/IronLanguages/ironpython3/blob/v3.4.0-alpha1/Documentation/differences-from-c-python.md
import sys
sys.path.append('C:\Users\Georg\AppData\Local\Programs\Python\Python310\lib')
import os
import math
print(sys.implementation.name)
print(type(1<<64))
print(isinstance(1<<64, int))
print('\ud83d\udf0b')
print('abc:~~:zyz'.encode('utf-7'))