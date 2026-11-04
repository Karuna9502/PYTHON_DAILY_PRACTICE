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

