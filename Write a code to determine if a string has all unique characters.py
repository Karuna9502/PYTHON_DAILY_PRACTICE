# Write a code to determine if a string has all unique characters
string = input("Enter string: ")
seen = set()

for ch in string:

    if ch in seen:
        print("String does not have unique characters")
        break

    seen.add(ch)

else:
    print("String has all unique characters")

(set() displays like {} when empty)
