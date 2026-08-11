'''****
   ****
   ****
   ****'''

for i in range(4):
    for j in range(4):
        print("*",end='')
    print()

'''*
   **
   ***
   ****
   *****'''


for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()

'''1
   12
   123
   1234
   12345'''

for i in range(6):
    for j in range(1,i+1):
        print(i,end='')
    print()

'''*****
   ****
   ***
   **
   *'''

for i in range(6,0,-1):
    for j in range(i-1):
        print("*",end='')
    print()

'''12345
   1234
   123
   12
   1'''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

'''   *
     ***
    *****
   *******
  *********'''

for i in range(1, 6):
    for j in range(5-i):
        print(' ',end='')
    for j in range(2*i-1):
        print("*",end='')
    print()

'''*********
    *******
     *****
      ***
       * '''

# Fixed version to print an inverted pyramid
for i in range(5, 0, -1):              # Loops down from 5 to 1
    for j in range(5 - i):             # Increases leading spaces each row
        print(' ', end='')
    for j in range(2 * i - 1):         # Decreases odd-numbered stars each row
        print("*", end='')
    print()                            # Moves to the next line

'''  *
    ***
   *****
  *******
 *********
 *********
  *******
   *****
    ***
     *'''

for i in range(5):
    for j in range(5-i):
        print(' ',end='')
    for j in range(2 * i +1):
        print("*",end='')
    print()
for i in range(5,0,-1):
    for j in range(6-i):
        print(' ',end='')
    for j in range(2 * i - 1):
        print("*",end='')
    print()

'''*
   **
   ***
   ****
   *****
   ****
   ***
   **
   *'''

for i in range(5):
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(5, 1, -1):
    for j in range(i-1):
        print("*",end='')
    print()

'''1
   10
   101
   1010
   10101'''


for i in range(5):
    if i % 2 == 0:
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start,end='')
        start = 1 - start
    print()

'''1      1   
   12    21
   123  321  
   12344321'''


for i in range(1, 5):
    # Print left increasing numbers
    for j in range(1, i + 1):
        print(j, end='')
        
    # Print spaces in between rows
    for j in range(2 * (4 - i)):
        print(' ', end='')
        
    # Print right decreasing numbers
    for j in range(i, 0, -1):
        print(j, end='')
        
    print()

'''1
   2 3
   4 5 6
   7 8 9 10
   11 12 13 14 15'''

n = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=' ')
        n += 1
    print()

'''A
   AB
   ABC 
   ABCD
   ABCDE'''

for i in range(5):
    for j in range(i+1):
        print(chr(65 + j), end='')
    print()

'''ABCDE
   ABCD
   ABCD
   ABC
   AB
   A'''


for i in range(5,0,-1):
    for j in range(i):
        print(chr(65 + j), end='')
    print()

'''A
   BB
   CCC
   DDDD
   EEEEE'''

for i in range(5):
    for j in range(i+1):
        print(chr(65+i),end='')
    print()

'''    A
      ABA
     ABCBA
    ABCDCBA
   ABCDEDCBA'''

n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Increasing letters
    for j in range(i):
        print(chr(65 + j), end="")

    # Decreasing letters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()

'''   E
      DE
      CDE
      BCDE
      ABCDE
     '''


n = 5

for i in range(n):
    for j in range(i + 1):
        print(chr(69 - i + j), end="")
    print()

'''         **********
            **** ****
            ***   ***
            **     **
            *       *
            *       *
            **     **
            ***   ***
            **** ****
            *********'''



n = 5

# Upper Half
spaces = 0

for i in range(n, 0, -1):

    for j in range(i):
        print("*", end="")

    for j in range(spaces):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

    spaces += 2
  # Lower Half
spaces = 2 * (n - 1)

for i in range(1, n + 1):

    for j in range(i):
        print("*", end="")

    for j in range(spaces):
        print(" ", end="")

    for j in range(i):
        print("*", end="")

    print()

    spaces -= 2


