#Write a code to check if two given strings are anagrams of each other

word1 = input("Enter a word : - ")
word2 = input("Enter another word : - ")

list1 = list(word1)
list2 = list(word2)

list1.sort()
list2.sort()

if list1 == list2:
    print(f"{word1} and {word2} are anagrams")
else:
    print("Not anagrams")

Input
↓
Convert to list
↓
Sort
↓
Compare
