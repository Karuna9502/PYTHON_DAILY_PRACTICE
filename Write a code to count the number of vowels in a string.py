# Write a code to count the number of vowels in a string


char = input("Enter string :- ")
count = 0
for ch in char:
    if ch.lower() in "aeiou":
        count = count + 1
print("number of vowles is", count)
