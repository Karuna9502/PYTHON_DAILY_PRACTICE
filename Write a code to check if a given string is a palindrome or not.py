#Write a code to check if a given string is a palindrome or not

string = input("Enter a string : ")

i = len(string) - 1
r = ""

while i >= 0:
    r = r + string[i]
    i -= 1

if string == r:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
