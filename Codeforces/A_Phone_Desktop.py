""" 
Read x and y
    Calculate screens_needed = ceil(y / 2)
    Calculate total_cells_used = y * 4
    Calculate unused_cells = (screens_needed * 15) - total_cells_used
    If unused_cells is enough for 1x1 icons:
        Print screens_needed
    Else:
        Calculate remaining_1x1 = x - unused_cells
        Calculate additional_screens = ceil(remaining_1x1 / 15)
        Print screens_needed + additional_screens
"""

import math

T = int(input())  # total test cases

for _ in range(T):
  # handle each test case here
  x, y = map(int, input().split())

  screens_used = math.ceil(y/2)  # minimum screens needed for 2x2
  unused_cells = (screens_used*15) - (y*4)  # unused cells after placing 2x2

  if unused_cells >= x:  # enough cells for 1x1?
    print(screens_used)
    continue

  # otherwise add more screens
  x -= unused_cells  # use `unused_cells`, place remaining 1x1 on new screens
  screens_used += math.ceil(x/15)
  print(screens_used)
