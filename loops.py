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


#Print numbers from 1 to 5 using range().
for j in range(1,6):
    print(j)

#Print squares of numbers from 1 to 5 using a loop.  
for s in range(1,6):
    print(f"square of {s} = ", s*s)

#Print only even numbers from 1 to 10.
for even in range(1,11):
    if even % 2 == 0:
        print(even)


#Print the sum of numbers in the list [1,2,3,4,5]. 
list2 = [1,2,3,4,5]
total = 0
for k in list2:
    total = total + k
print("the sume of list is", total)

   
