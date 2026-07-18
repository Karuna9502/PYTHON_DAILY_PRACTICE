# Create a dictionary student with keys: "name", "age", "course". Print all the keys using keys().
student = {
    'name' : 'karuna',
    'age' : 23,
    'course' : 'MCA'
}

print(student.keys())

print('-------')

for key in student.keys():
    print(key)

print('-------')  

print(list(student.keys()))

print('-------')  
#Print all the values of the dictionary using values().
print(student.values())

print('-------')  
#Print all key-value pairs using items().
print(student.items())

print('-------') 
#Safely access the "course" key using get().
print(student.get('course'))

print('-------') 
#Try to access a non-existent key "email" using get() and provide a default value "Not Available".
print(student.get('email', "Not Available"))

print('-------') 
#Add a new key "email" with value "student@example.com" using update().
student.update({"email":"student@example.com"})
print(student)

print('-------') 
#Change the "age" value to 23 using update().
student.update({'age':24})
print(student)

print('-------') 
#Remove the key "course" using pop().  
student.pop("course")
print(student)

print('-------') 
#Remove the last inserted key-value pair using popitem() 
student.popitem()
print(student)

print('-------') 
#Make a shallow copy of the dictionary using copy(). 
shallow_copy = student.copy()
print(shallow_copy)

print('-------') 
#Use setdefault() to add a key "phone" with value "000-000-0000" if it doesn’t exist.
student.setdefault("Phone","000-000-0000")
print(student)

print('-------') 
#Clear all items from the dictionary using clear().
student.clear()
print(student)  

print('-------') 
#Create a nested dictionary with "marks" as another dictionary inside student. Access the "SQL" marks.
student1 = {
    'name' : 'karuna',
    'age' : 23,
    'marks': {
        'os': 85,
        'SQL': 90,
        'java': 88,
        'DSA' : 92
    }
}

print(student1['marks']['SQL'])


print('-------') 
#Loop through the dictionary and print all keys one by one.
for key in student1:
    print(key)

print('-------') 
for values in student1.values():
    print(values)

print('-------')  
for key, value in student1.items():
    print(key, ":", value)
