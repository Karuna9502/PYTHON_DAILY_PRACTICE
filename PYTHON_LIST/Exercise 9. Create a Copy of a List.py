'''Practice Problem: Create a copy of an existing list 
so that modifying the copy does not change the original.'''

original = ["Apple", "Banana", "Cherry"]

# Create a true copy
new_copy = original.copy()

# Prove they are independent
new_copy.append("Date")

print(f"Original: {original}")
print(f"Copy: {new_copy}")

'''
By using .copy(), we allocate a new block of memory for new_copy.
 When we add “Date” to it, the original remains unaffected.
 Shallow Copy: Note that .copy() creates a “shallow” copy. If the list contained other lists inside it, those nested lists
 would still be shared. For “deep” independence, you’d use the copy module’s deepcopy() function.'''
