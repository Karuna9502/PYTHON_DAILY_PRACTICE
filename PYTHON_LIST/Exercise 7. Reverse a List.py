'''Practice Problem: Take a list and reverse the order of its elements.'''


input = [100,200,200,400,500]
reversed_list = input[::-1]
print(reversed_list)

'''[::-1]: This is “Pythonic” shorthand for slicing.
 It tells Python to start at the end, 
stop at the beginning, and move with a “step” of -1'''
