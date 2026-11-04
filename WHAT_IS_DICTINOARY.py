# Q1 ASK FOR THE SUBJECT NAME AND MARKS FROM THE USER AND KEEP ADDING IT TO THE DICTIONARY  
marks = {}
subject_count = int(input("enter the number of subjects = ")) 
for _ in range(subject_count): # underscore ka koi kaam nhi hai, bas loop chana hai 
    sub_name = input("enter the subjects name = ")
    sub_marks = int(input(f"enter marks for {sub_name} = "))
    marks[sub_name] = sub_marks
print(marks)
