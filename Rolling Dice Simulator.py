import random
print("ROLLING DICE SIMULATOR")
s = int(input("Digit how many sides does the dice have:"))
t = int(input("Digit how many times it will be rolled:"))
for i in range(t):
    print(random.randrange(1,s+1))
