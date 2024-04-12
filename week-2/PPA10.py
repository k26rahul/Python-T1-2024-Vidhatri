x = float(input())

integer_part_of_x = int(x)

# Case 1: Number is an integer
if integer_part_of_x == x:
  print(integer_part_of_x)  # floor
  print(integer_part_of_x)  # ceil

# Case 2: Not an integer. Positive value
elif x > 0:
  print(integer_part_of_x)  # floor
  print(integer_part_of_x + 1)  # ceil
