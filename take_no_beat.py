import random
import time

n = input("Please enter en integer value.: ")
n = int(n)

for i in range(n):
    print(n - i)
    time.sleep(random.triangular(0.5, 1.5, 1.0))
print("complete")
