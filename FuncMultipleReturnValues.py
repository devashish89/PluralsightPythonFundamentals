import numpy as np
import math as m

f = [120,10,30,40,60,100,90,5,6]
def minmax(lst):
    return np.min(lst), np.max(lst) ## multiple returns output as tuple

print(type(minmax(f)))

min, max = minmax(lst=f)

print("min: {} & max: {}".format(min, max))

print("min: {tup[0]} & max: {tup[1]}".format(tup = minmax(f)))

print("Math constants are pi: {m.pi} & exp: {m.e}".format(m=m))

print("Math constants are pi: {m.pi:.3f} & exp: {m.e:.3f}".format(m=m))