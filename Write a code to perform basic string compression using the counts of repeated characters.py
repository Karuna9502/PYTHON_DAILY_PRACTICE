 # Write a code to perform basic string compression using the counts of repeated characters
string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)-1):

    if string[i] == string[i+1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

compressed += string[-1] + str(count)

print("Compressed string:", compressed)
