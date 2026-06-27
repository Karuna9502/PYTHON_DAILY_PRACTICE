# Write a code to reverse a string

# method one
Name = "karuna"
method1 = Name[::-1]
print(method1)

#method two
number = "1,2,3,4,5,6,7,8,9,10"
method2 = ''.join(reversed(number))
print(method2)

#method three
s = "Python"

reverse = ""
i = len(s)-1

while i >= 0:
    reverse += s[i]
    i -= 1

print(reverse)
