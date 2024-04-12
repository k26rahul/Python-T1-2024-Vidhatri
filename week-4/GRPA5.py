# Print all points in the sequence that are nearest to P

n = int(input())

points = []
for i in range(n):
  point = list(map(int, input().split(',')))
  points.append(point)

p = list(map(int, input().split(',')))
px = p[0]
py = p[1]

distances = []
for point in points:
  point_x = point[0]
  point_y = point[1]
  dist = (
      (px - point_x)**2 + (py - point_y)**2
  ) ** 0.5
  # print(f'{point_x=}, {point_y=}, {dist=}')
  data = (point_x, point_y, dist)
  distances.append(data)

min_distance = float('inf')
for data in distances:
  dist = data[2]
  if dist < min_distance:
    min_distance = dist

for data in distances:
  dist = data[2]
  if dist == min_distance:
    print(f'{data[0]},{data[1]}')
