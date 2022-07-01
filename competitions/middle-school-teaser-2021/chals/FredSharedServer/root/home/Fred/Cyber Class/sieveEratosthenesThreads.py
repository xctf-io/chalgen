import numpy as np
import time
import _thread

def checkMultiple(i, x):
	multiple = 2*i;
	while(multiple < sizeOfArray):
		x[multiple] = 0
		multiple += i

np.random.seed(0)  # seed for reproducibility
sizeOfArray = 1000000000
x = np.random.randint(10, size=sizeOfArray)  # One-dimensional array

timeStart = time.time()
for i in range(sizeOfArray):
	x[i] = i
print("Finished creating list.")
for i in range(2, sizeOfArray):
	if(i != 0):
		#checkMultiple(i,x)
		_thread.start_new_thread(checkMultiple, (i,x, ))
		#time.sleep(.00001)
print("Finished eliminating composites.")
count = 0;
f = open('primes.txt', 'w')
for i in range(2, sizeOfArray):
	if x[i] > 0:
		f.write(str(x[i])+"\n")
		count += 1;
timeEnd = time.time()
outputString = str(timeEnd - timeStart) +  "seconds for "+  str(count) + " primes in range up to " +  str(sizeOfArray)
f.write(outputString)
print(timeEnd - timeStart, "seconds for", count, "primes in range up to", sizeOfArray)

