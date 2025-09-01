'''
Hollow_Equilateral_Triangle.py


Enter the row value:  5
    *
   * *
  *   *
 *     *
*********

'''

rows = int(input('Enter the row value:  '))


for i in range(1, rows+1):
    if i == 1:  # top row
        print(' '*(rows-i) + '*')
    elif i == rows:  # bottom row
        print('*' * ((rows*2)-1))
    else:  # middle rows
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')
