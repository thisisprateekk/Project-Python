"""Vectorized vs Loop Version in Python

This Python script compares the performance of a vectorized operation using NumPy’s np.dot function against a traditional loop-based implementation for computing the dot product of two large arrays. 
The script generates two random arrays of size 10,000,000 and measures the execution time for both methods, demonstrating the efficiency of vectorized operations over loops in numerical computations."""

import numpy as np
import time
def loop_version(a,b):
    x=0
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x

a = np.random.rand(10000000)
b = np.random.rand(10000000)

t1 = time.time()
c = np.dot(a, b)
t2 = time.time()

print(f"np.dot(a, b) =  {c:.4f}")
print(f"Vectorized version duration: {1000*(t2-t1):.5f} ms ")

t3 = time.time()
c = loop_version(a,b)
t4 = time.time()

print(f"my_dot(a, b) =  {c:.4f}")
print(f"loop version duration: {1000*(t4-t3):.5f} ms ")

t5 = 1000*((t4-t3)-(t2-t1))
print(f"the vectorized version is faster than the loop version by {t5:.5f} ms ")

