'''
Hollow Diamond
Enter the row value:  4
   *
  * *
 *   *
*     *
 *   *
  * *
   *

'''
rows = int(input('Enter the row value:  '))

for i in range(1, rows):
    if i == 1:  
        print(' '*(rows-i) + '*')
    else:  
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')
for i in range(rows, 0, -1):
    if i == 1: 
        print(' '*(rows-i) + '*')
    else:  
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')
