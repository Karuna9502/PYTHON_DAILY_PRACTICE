'''Practice Problem: Take a given list and modify it through five specific actions:

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.'''

input = [100, 50,400,500]
input[1] = 200 
print(input)
input.append(600)
print(input)
input.insert(2,300)
print(input)
input.remove(600)
print(input)
input.pop(0)
print(input)
