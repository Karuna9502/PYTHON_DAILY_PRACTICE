# Q1 ASK FOR THE SUBJECT NAME AND MARKS FROM THE USER AND KEEP ADDING IT TO THE DICTIONARY  
marks = {}
subject_count = int(input("enter the number of subjects = ")) 
for _ in range(subject_count): # underscore ka koi kaam nhi hai, bas loop chana hai 
    sub_name = input("enter the subjects name = ")
    sub_marks = int(input(f"enter marks for {sub_name} = "))
    marks[sub_name] = sub_marks
print(marks)
# OUTPUT 
enter the number of subjects =  3
enter the subjects name =  math
enter marks for math =  87
enter the subjects name =  science
enter marks for science =  89
enter the subjects name =  sst
enter marks for sst =  90
{'math': 87, 'science': 89, 'sst': 90}

# Q2: CONVERT TWO LISTS INTO A DICTIONARY. MARK TWO LISTS ON YOUR OWN IF THEY ARE THE SAME LENGTH AND CONVERT THEM TO A DICTIONARY
list1 = ["ten", "twenty", "thirty"]
list2 = [10,20,30]
combine_list ={}
for i in range(0, len(list1)): 
    combine_list[list1[i]] = list2[i]
print(combine_list)
# OUTPUT 
{'ten': 10, 'twenty': 20, 'thirty': 30}


# Q3: Write a Python program to sum all the items in a dictionary 
my_result = { "math":78, "science": 90, "sst":80, "english":98, "hindi": 95}
sum_of_items = 0 
for v in my_result.values():
    sum_of_items += v 
print("sum of marks = ", sum_of_items)

print(sum(list(my_result.values())))
#OUTPUT 
sum of marks =  441
441

# Q4: ASK FOR A STRING FROM THE USER. DISPLAY THE DICTIONARY WHERE EACH KEY IS A CHARACTER AND THE VALUE IS THE FREQUENCY OF THAT CHARACTER IN THAT STRING
my_string = input("enter a string = ")
frq = {}
for ch in my_string:
    if ch in frq:
        frq[ch] += 1 
    else:
        frq[ch] = 1
print(frq)
#OUTPUT 
enter a string =  karuna
{'k': 1, 'a': 2, 'r': 1, 'u': 1, 'n': 1}

# Q5 STORE "NAME" OF A STUDENT LIST OF 5 MARKS OF THAT STUDENT AS A VALUE. STORE AT LEAST 5 STUDENT NAMES. PRINT THE SUM AND PERCENTAGES OF ALL THE STUDENTS. 
st_data = {
    "student1" : [67,89,65,76,45],
    "student2": [76,89,90,98,77],
    "student3": [98,76,98,76,89],
    "student4": [98,76,54,23,63],
    "student5":[78,90,87,55,78]
}
for k,v in st_data.items():
    total = 0 
    for marks in v:
        total += marks
        percentage = total / 500 * 100
    print(f"{k} has scored {total} marks, percentage = {percentage:.2f}")
#OUTPUT 
student1 has scored 342 marks, percentage = 68.40
student2 has scored 430 marks, percentage = 86.00
student3 has scored 437 marks, percentage = 87.40
student4 has scored 314 marks, percentage = 62.80
student5 has scored 388 marks, percentage = 77.60

# Q6 STORE MARKS OF 5 DIFFERENT SUBJECTS IN A DICTIONARY. ASK FOR THE SUBJECT NAME AS INPUT FROM THE USER. PRINT THE MARKS OF THE SUBJECT ENTERED BY THE USER. IF THE SUBJECT DOES NOT EXIST, PRINT "INVALID"  
subject_marks = {
    "maths":90, 
    "science": 89, 
    "sst": 78, 
    "english": 54, 
    "hindi": 90
}
subject_name = input("enter the subject name = ")  
if subject_name in subject_marks:
    print(subject_marks[subject_name])
else:
    print("invalid")
#OUTPUT
enter the subject name =  maths
90

