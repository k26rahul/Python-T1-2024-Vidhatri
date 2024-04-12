n = int(input())

zero_matrix = []

for _ in range(1, n+1):
  row = [0 for _ in range(1, n+1)]
  zero_matrix.append(row)

for i in range(n):
  for j in range(n):
    if i == j:
      zero_matrix[i][j] = 1

# print(zero_matrix)

for row in zero_matrix:
  row = map(str, row)
  print(','.join(row))
