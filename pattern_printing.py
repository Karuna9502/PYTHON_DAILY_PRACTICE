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
