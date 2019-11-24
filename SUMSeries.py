# {a,a+k,a+2k,a+3k,...}
from datetime import datetime

number = 10000      # Total number
a = 20              # start number
d = 1               # different for each near number
total = 0
print("Total number {} numbers.  Start number is {}.  Common different is {}.".format(number, a, d))

print("Basic method")
lastNumber = a+(number-1)*d
startTime = datetime.now()
for n in range(a, lastNumber+d, d):   # Basic method
    total += n
processTime = (datetime.now()-startTime).microseconds
print("Process time : {0:<12} Microseconds".format(processTime))
print("Total SUM = ", total)

print("\nSeries sum method")
startTime = datetime.now()
total = (number/2)*(2*a+(number-1)*d)
processTime = (datetime.now()-startTime).microseconds
print("Process time : {0:<12} Microseconds".format(processTime))
print("Total SUM = ", int(total))

