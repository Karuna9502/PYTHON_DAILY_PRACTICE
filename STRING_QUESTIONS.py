# ASK A STRING FROM USER. COUNT HOW MANY ALPHABETS ARE THERE IN THAT STRING
user_input = input("enter a string := ")
count = 0
for ch in user_input:
    if ch.isalpha():
        count += 1    
print(f"this is the count of alphabets from your given string {user_input}: -", count)
# without using methods of string
user_input = input("enter a string := ")
count = 0
for ch in user_input:
    acsii = ord(ch)
    if (acsii >= 65 and acsii <= 90) or (acsii >= 97 and acsii <= 122 ):
        count += 1
print(count)

# ASK A STRING FROM USER COUNT THE NUMBER OF UPPERCASE AND LOWERCASE CHARACTER IN THAT STRING 
user_input1 = input("enter a string = ")
upper = 0
lower = 0
for ch in user_input1:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
# without string methods 
for ch in user_input1:
    asc = ord(ch)
    if asc >= 65 and asc <= 90:
        upper += 1
    elif asc >=97 and asc <= 122:
        lower += 1
print(upper)
print(lower)
