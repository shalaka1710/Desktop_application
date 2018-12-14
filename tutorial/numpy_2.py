import numpy as np
import sys
import time

SIZE=10000

l1 = range(SIZE)
l2 = range(SIZE)

start1 =time.time()
result= [(x,y) for x,y in zip(l1,l2)]
print((time.time()-start1)*1000)

A1=np.arange(SIZE)
A2=np.arange(SIZE)

start = time.time()
result=A1+A2
print((time.time()-start)*1000)

np_array=np.array([(1,2,9),(4,5,6)])
print('dimention of array : ',np_array.ndim)
print('Item size is : ',np_array.itemsize)
print('Date type of each elelment : ',np_array.dtype)

print("size of array : ",np_array.size)
print("size of array : ",np_array.shape)

print(np_array)
print(np_array.reshape(3,2))
print("Slicing element  :",np_array[0,1])
print("Slicig : ",np_array[1:,2])  #slicing on particualr element#
print(np.linspace(1,3,10)) # print the values between start and end position


print("Maximun value in array :",np_array.max())
print("Minimun value in array :",np_array.min())
print("Sum value in array :",np_array.sum())

# axis 1 -row , axis 0 - column
print("sum of all rows ",np_array.sum(axis=1))
print("sum of all column ",np_array.sum(axis=0))

#square root of array
print("square root of the array : ",np.sqrt(np_array))
print("standart devition is : ",np.std(np_array))

#addition - * / using np array
array1=np.array([(16,23,42),(34,5,66)])
array2=np.array([(1,2,4),(4,5,6)])

print("Addition of two array : ",array1+array2)
print("substraction of two array : ",array1-array2)
print("multiplication of two array : ",array1*array2)
print("division of two array : ",array1/array2)


#concatination of two array
print("vertical stacking of array :",np.vstack((array1,array2)))
print("horizontal stacking of array : ",np.hstack((array1,array2)))
print("another way to concat : ",array2.ravel())
print("another way to concat : ",np.ravel((array1,array2)))