# if module i.e function is in same project folder as my program
import myfunctions as f

#if module is in different package inside same project
#import modpack.myfunctions as f

"""
if module was present somewhere else in the system for eg in mycode folder in C drive
import sys
sys.path.append("C:\mycode")
import myfunctions as f
"""

square = f.area_of_square(30)
print(square)

triangle = f.area_of_traingle(20,85)
print(triangle)
