#Write a code to find all occurrences of a given substring within another string

main = input("Enter main string: ")
sub = input("Enter substring: ")

positions = []

for i in range(len(main) - len(sub) + 1):
    if main[i:i+len(sub)] == sub:
        positions.append(i)

print("Occurrences found at indexes:", positions)
