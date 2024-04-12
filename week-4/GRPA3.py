n = int(input())

# for sq. matrix: m, n, p = `n`

# m * n
matrix_a = []
for i in range(n):
  row = list(map(int, input().split(',')))
  matrix_a.append(row)

# n * p
matrix_b = []
for i in range(n):
  row = list(map(int, input().split(',')))
  matrix_b.append(row)

# skeleton (m * p)
product_matrix = [[
    0 for j in range(n)  # no. of cols (p)
] for i in range(n)]  # no. of rows (m)

for i in range(n):
  for j in range(n):
    sigma = 0

    for k in range(n):
      sigma += matrix_a[i][k] * matrix_b[k][j]

    product_matrix[i][j] = sigma

# print(product_matrix)

for row in product_matrix:
  row = list(map(str, row))
  print(','.join(row))
