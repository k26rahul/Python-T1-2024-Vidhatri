n = int(input())

zero_matrix = [
    [0 for _ in range(1, n+1)]
    for _ in range(1, n+1)
]

for i in range(n):
  for j in range(n):
    if i == j:
      zero_matrix[i][j] = 1

print(zero_matrix)
