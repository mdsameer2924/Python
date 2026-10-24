from array import *

a1 = array("i", [23, 5, 9])
print(a1)

for x in a1:
    print(x, end=" ")
print()

for i in range(3):
    print(a1[i], end=" ")
print()
print(f"lenght of an array: {len(a1)}")

## we can use while condition:
i = 0
while i < len(a1):
    print(f"idx {i}, value: {a1[i]}")
    i = i + 1

## Array methods
a1.append(7)
for y in a1:
    print(y)
