🔁 For Loop Practice Questions
Basic Level (1–10)

#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)

#Print each character of the string "Karuna".
name = 'karuna'
for s in name:
    print(s,end='')

#Print all elements of a list: [10, 20, 30, 40, 50].
list1 =  [10, 20, 30, 40, 50]

for l in list1:
    print(l)

#Print all keys of a dictionary: {"name":"Karuna","age":23,"course":"MCA"}.
student = {
    "name":"Karuna",
    "age": 23,
    "course":"MCA"
}

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key,value)
