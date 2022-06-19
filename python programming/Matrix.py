import array
from numpy import *

arr1 = array([
                [1, 2, 3, 4, 8, 6],
                [9, 8, 7, 6, 3, 5]
            ])


print(arr1.dtype)
print(arr1.ndim)
print(arr1.size)
arr2 = arr1.flatten()
print(arr2)
arr3 = arr2.reshape(3, 4)
print(arr3)
arr4 = arr2.reshape(2, 2, 3)
print(arr4)
