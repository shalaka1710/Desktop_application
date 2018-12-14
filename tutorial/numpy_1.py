import numpy as np
import time
import sys

l1 = range(100)
print(l1)
print("Size of list",sys.getsizeof(5)* len(l1))

np_array = np.arange(100)
print(np_array)

print("Size of numpy array :",np_array.size* np_array.itemsize )