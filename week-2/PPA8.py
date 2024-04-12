# x_map = {
#     "A": 1,
#     "B": 2,
#     "C": 3,
#     "D": 4,
#     "E": 5,
#     "F": 6,
#     "G": 7,
#     "H": 8
# }

# x1 = x_map[start[0]]
# x2 = x_map[end[0]]

start = input()
end = input()

y1 = int(start[1])
y2 = int(end[1])

x1 = ord(start[0]) - 64
x2 = ord(end[0]) - 64

if x1 - x2 == y1 - y2:
  print('YES')
else:
  print('NO')
