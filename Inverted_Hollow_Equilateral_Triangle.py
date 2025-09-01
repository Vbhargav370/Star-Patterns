'''
Inverted Hollow Equilateral Triangle
Enter the row value:  5
*********
 *     *
  *   *
   * *
    *

'''
rows = int(input('Enter the row value:  '))


for i in range(rows, 0, -1):
    if i == 1: 
        print(' '*(rows-i) + '*')
    elif i == rows:  
        print('*' * ((rows*2)-1))
    else:  
        print(' '*(rows-i) + '*' + ' '*((2*i)-3) + '*')


