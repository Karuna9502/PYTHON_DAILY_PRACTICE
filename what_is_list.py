karuna = [1,2,33.3,False,"karuna"]
print(karuna)
print(type(karuna))


#INDEXING/POSITION IN LIST 
x = [45,32,15,"C&D", 198.88, 61]
print(x[0])
print(len(x))
print(x[-1])
print(type(x[1]))
#print(x[100])
#print(x[-10])

#ITREATING THROUGH LIST 
for i in x:
    print(i)
print("------------------------------------")
for i in range(len(x)):
    print(x[i])
print("-------------------------------------")
for i in range(0, len(x)):
    print(i) # index print ho rha hai 

# MAKE A YOUR OWN LIST. PRINT THE LIST IN REVERSE 
a = [4,-98, "code and debug", 22.22, 100]
for i in range(len(a)-1,-1,-1):
    print(a[i], end=" ")

print("-------------------------------------------")
# Make your own list. print all the even numbers present in the list
b = [2,4,6,8,10,22,12,35,67,32,57,865,3257,84,35,7,3,78,75]
# itration by value
for i in b:
    if i % 2 == 0:
        print(i, end=" ")
print("----------------------------------------------")
# itration by index
for i in range(0, len(b)):
    if i % 2 == 0:
        print(b[i], end=" ")
print("--------------------------------")
for i in range(0, len(b)):
    if i % 2 == 0:
        print(i, end=" ") # index printing
print("-------------------------------------------------")
# MAKE YOUR OWN LIST. PRINT ALL THE ODD NUMBERS PRESENT IN THE LIST 
c = [23,4,8,654,3,25,7,8,64,3,4,6,8,7,4,3,2,0,4,7,80,9]
for i in c:
    if i % 2 != 0:
        print(i, end=" ")
print("--------------------------------------------------")
# MAKE YOUR OWN LIST. PRINT ALL THE ELEMENT PRESENT AT EVEN INDEX POSITION
d = ["karuna",12,34,56,76,5,4,5,7,"False",8,6,4,2,3,5.43,7,"anisha",8,66,5,44,6,7,8,6,5,444,5,5,6,677,8,8,9]
for i in range(0, len(d)):
    if i % 2 == 0:
         print(d[i], end=" ")
print("-----------------------------------------------------")
# MAKE YOUR OWN LIST PRINT THE SUM OF ALL ELEMTS PRESENT IN THAT LIST 
e = [45,6,7,86,95,4,3,3,76.5,4,5.7,5,4,3.3,5,4.3,4,6,4,2,1,4,0,7,8,6,4]
total = 0
for i in e:
    total = total + i
print("sum of element in list",total)
print("------------------------------------------------")
#MAKE YOUR OWN LIST.COUNT THE NUMBER OF EVEN NUMBER PRESENT IN THAT LIST
f = [34,5,6,7,8,5,3,3,2,2,4,4,5,567,7,8,8,6,6434,776,6,7,7,77,4,3,45,6,8,6,65.6,4,2,3,5,7,9,7]
count = 0
for i in f:
    if i % 2 == 0:
        count = count + 1
print("number of even elements in the list",count)
print("-------------------------------------------------------")
# MAKE YOUR OWN LIST. COUNT HOW MANY NUMBER ARE DIVISIBLE BY BOTH 2 AND 5 IN THAT LIST
g = [23,4,5,6,7,10,8,9,8,8,7,6,98,87,6,15,65,3,2,54,4,5,5,4,4,5,33,6,7,765,4,3,3,44,23,3,4,3,32,22.3]
count = 0
for i in g:
    if i % 2 == 0 and i % 5 == 0:
        count = count + 1
print("count of elements that is divisible by 3 and 5 both ", count)
print("------------------------------------------------------------")
# MAKE YOUR OWN LIST .FIND THE SUM OF ALL EVEN NUMBER PRESENT IN THAT LIST
h = [34,56,76,43,2,1,3,4,88,6,8,0,8,67,5,66,3,4,6,8,65,6]
totall = 0
for i in h:
    if i % 2 == 0:
        totall = totall + i 
print(totall)
print("-------------------------------------------------------")
# MAKE YOUR OWN LIST FIND THE SUM OF ALL NUMBERs DIVISIBLE BY 3 0R 4
ii = [34,5,42,65,3,6,6,4,5,4,6,7,4,3,54,3,4,5,7,6,65,4,34,3,2,3,5,6,55,8,7,6]
totalll = 0
for i in ii:
    if i % 3 == 0 or i % 4 == 0:
        totalll = totalll + i
print("sum of number which is divisible by 3 and 4", totalll)
print("--------------------------------------")
# MAKE YOUR OWN LIST. PRINT HOW MANY POSTIVIE AND NEGATIVE NUMBERS ARE HERE
j = [-3,-4,-53,-43,21,-2,34,36,7,54,3,35,6,4,34,-54,6,4,2,2,5,65,4,3,3,4,67]
positive = 0
negative = 0
for i in j:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print("Total number of positive in a list is : =", positive)
print("Total number of negative in a list is : =", negative)
print("------------------------------------------------------------")
# MAKE YOUR OWN LIST PRINT THE LARGEST NUMBER PRESENT IN THAT LIST
k = [54,34,56,78,98,65,43,23,45,678,76]
largest = 0
for i in k:
    if i > largest:
        largest = i
print("The largest element is",largest)
print("-------------------------------------")
k1 = [-3,-4,-5,-6,-7,-2,-5,-1,-4,-5]
large = k1[0]
for i in k1:
    if i > large:
        large = i
print("The largest negative lement is :- ", large)
print("--------------------------------------------")
# MAKE YOUR OWN LIST PRINT THE SMALLEST NUMBER PRESENT IN THAT LIST
l = [3,4,6,3,2,8,7,8,5,3,2,-2]
smallest = l[0]
for i in l:
    if i < smallest:
        smallest = i
print("The smallest number in this list is := ", smallest)
# FUNCTION AND METHODS OF STRING 
m = [43,56,78,6,43,55,33,6,7]
print("---FUNCTION--function is a pre- define code -")
print(len(m))
print(sum(m))
print(max(m))
print(min(m))
print("---METHODS- is also a function but only used by list list ke methods")
print(m)
m.append(34)
m.append("Karuna")
m.append(False)
m.append(-98)
print(m)
m.insert(3,"python")#index , value
m.insert(400, "Aditya")#inserting value by index in any position
print(m)
m[0] = "karuna-kumari"#updating value by index
m[-1] = "karuna-kumari"
#m[50] = "karuna-kumari" 
print(m)
print("------Deleting------")
m.pop()# by default last wala delete hoga
m.pop(3)# remove by postion
m.remove(6)#remove by value, if 2 6 hota toh toh phla 6 delete hoga
del m[0]# ye list ke alwa bhi use hota hai 
# m.clear() - clear the list 
print(m)

print("---------------------------------------------------------------------")
# WRITE A PROGRAM THAT PROMPTS THE USER TO SPECIFY THE LENGTH OF A LIST AND THEN REQUESTS NUMBER TO POPULATED THAT LIST DISPLAY THE FINAL LIST AS THE OUTPUT
list_len = int(input("enter the length of list : - "))
Result = []
for i in range(1,list_len+1):
    num = int(input(f"enter a number at postion of {i} :- "))
    Result.append(num)
print(Result)
print("----------------------------------------------------------------------")
# CREATE A LIST AND PROMPT THE USER FOR AN OLD NUMBER FOLLOWED BY A NEW NUMBER IF THE OLD NUMBER EXISTS IN THE LIST, REPLACE IT WITH THE NEW NUMBER PROVIDED BY THE USER 
replac_list = [23,45,67,89,15]
print(replac_list)
old_number = int(input("enter the old number : - "))
new_number = int(input("enter the number u wanna replace with : - "))
for i in range(0,len(replac_list)):
    if replac_list[i] == old_number:
        replac_list[i]  = new_number
print(replac_list)
print("--------------------------------------------------------------------")
# REMOVE ALL THE EVEN NUMBERS FROM THE LIST 
user_list = input("enter the list of numbers :- ")
intt_list = [int(x) for x in user_list.split(",")]
print("user list :- ",intt_list)
oddlist = []
for i in intt_list:
    if i % 2 != 0:
        oddlist.append(i)
print("odd list :- ", oddlist)
# HOME WORK KI LIST SE KAISE EVEN NUMBER REMOVE KR DENGE 
print("-------------------------------------------------------------------")
#ASK THE USER FOR A NUMBER THEN,FORM A LIST OF NUMBER REMOVE ALL THE NUMBERS THAT CAN BE DIVIDED BY THAT NUMBER THE USER ENETRED 
divisible = [2,3,4,5,6,7,87,8,9,7,6,56,6,7,7,6,5,4,3,2,6,3,4,5] 
print(divisible)
not_divident = []
divident = int(input("enter a number you wanna divided with :- "))
for i in divisible:
    if i % divident != 0:
        not_divident.append(i)
print("these are the number which is not divided by the number you have emtered:- ",not_divident)
print("-----------------------------------------------------------------")
# GENERATE A LIST OF AT LEAST 10 NUMBERS THEN, CREATE TWO SEPARATE LISTS CALLED ODD AND EVEN PUT ALL THE ODD NUMBERS FROM THE ORIGINAL LIST INTO THE ODD LIST AND ALL THE EVEN NUMBER INTO THE EVEN LIST
numbers = [2,3,4,5,6,7,8,8,9,7,6,4,2,3,4]
odd = []
even = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("ODD NUMBER:- ", odd)
print("EVEN NUMBER:-", even)
print("--------------------------------------------------------------------")
# START BY CREATING TWO SEPARATE LISTS WITH RANDOM NUMBERS. THEN CREATE A THIRED LIST THAT MERGERS THE NUMBERS FROM THE FIRST SECOND LISTS TOGETHER 
list1 = [1,2,3,4,5]
list2 = [11,12,13,14]
list3 = list1 + list2
print(list3)
list1 = [1,2,3,4,5]
list2 = [11,12,13,14,15]
list3 = []
for i in list1:
    list3.append(i)
for i in list2:
    list3.append(i)
print(list3)


