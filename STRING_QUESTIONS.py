# ASK A STRING FROM USER. COUNT HOW MANY ALPHABETS ARE THERE IN THAT STRING
user_input = input("enter a string := ")
count = 0
for ch in user_input:
    if ch.isalpha():
        count += 1    
print(f"this is the count of alphabets from your given string {user_input}: -", count)
