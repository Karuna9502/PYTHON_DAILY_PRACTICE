'''Exercise Purpose: While sum is built-in, “product” often requires you to think
 about how to accumulate values. 
This exercise reinforces the concept of an “accumulator variable” in a loop.'''

result = 1
input = [2,3,5,7]
for i in input:
    result = result * i

print(f"Product : {result}")
