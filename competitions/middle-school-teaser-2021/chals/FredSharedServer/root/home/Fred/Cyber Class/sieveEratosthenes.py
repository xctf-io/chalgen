import numpy as np
import time
np.random.seed(0)  # seed for reproducibility
sizeOfArray = 1000000000
x = np.random.randint(10, size=sizeOfArray)  # One-dimensional array
timeStart = time.time()
for i in range(sizeOfArray):
	x[i] = i
for i in range(2, sizeOfArray):
	if(i != 0):
		multiple = 2*i;
		while(multiple < sizeOfArray):
			x[multiple] = 0;
			multiple += i;
count = 0;
for i in range(2, sizeOfArray):
	if x[i] > 0:
		print(x[i])
		count += 1;
timeEnd = time.time()
print(timeEnd - timeStart, "seconds for", count, "primes in range up to", sizeOfArray)

