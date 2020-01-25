"""
Finished running reverse 1000 times:
1.1531908512115479

time: 0.03629422187805176

Finished running slice reverse 1000 times:
20.960039377212524

Finished running reversed() 1000 times:
0.0007898807525634766

time: 0.05808210372924805
##hello dad"""

from time import time

l = list(range(1000000))

start = time()
# loop through a thousand
for x in range(1000):
	l.reverse()
end = time()
print("Finished running reverse 1000 times:")
print(end-start)

# Iterate through real list
start = time()
for y in l:
	pass
end = time()
print(f"time: {end-start}")


start = time()
for x in range(1000):
	l = l[::-1]
end = time()
print("Finished running slice reverse 1000 times:")
print(end-start)


start = time()
for x in range(1000):
	b = reversed(l)
end = time()
print("Finished running reversed() 1000 times:")
print(end-start)


b = reversed(l)
start = time()
for y in b:
	pass
end = time()
print(f"time: {end-start}")

