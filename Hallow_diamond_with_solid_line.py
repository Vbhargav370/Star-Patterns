'''
Enter the row value:  6
     *
    * *
   *   *
  *     *
 *       *
***********
 *       *
  *     *
   *   *
    * *
     *
'''
rows = int(input('Enter the row value:  '))

for i in range(1, rows):
    if i == 1:  # top row
        print(' '*(rows-i) + '*')
    elif i == rows:  
        print('*' * ((rows*2)-1))
    else:  # middle rows
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')
for i in range(rows, 0, -1):
    if i == 1:  # top row
        print(' '*(rows-i) + '*')
    elif i == rows:  # bottom row
        print('*' * ((rows*2)-1))
    else:  # middle rows
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')
