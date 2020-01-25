from time import time

l = list(range(100000))
start = time()

loop = range(1000) #loop thru 1000x
for x in loop:
	l.reverse() #reverse whole array

end = time()

print("Finished running reverse 1000 times in: ")
print(end-start)

start = time()
for x in range(1000):
	l = l[::-1] #creathing new list
end = time()
print("Finished running slice reverse 1000 times in: ")
print(end-start)

start = time()
for x in range(1000):
	b = reversed(l) #reverse iterator; doesnt create list
end = time()
print("Finished running reversed() 1000 times in: ")
print(end-start)
