'''Practice Problem: Given a list of integers, 
iterate through the items and count how many are even and how many are odd.'''
Even_Number = []
Odd_Number = []
Input = [10,21,4,45,66,93,11]
for i in Input:
    if i % 2 == 0:
        Even_Number.append(i) 
    else:
        Odd_Number.append(i)
        
print("Even numbers: ", Even_Number)
print("Even numbers: ", len(Even_Number))
print("Odd numbers: ", Odd_Number)
print("Even numbers: ", len(Odd_Number))
