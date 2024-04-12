n = int(input())

mat = []

for i in range(n):
  row = list(map(int, input().split()))
  mat.append(row)

scalar = int(input())

for i in range(n):
  for j in range(n):
    mat[i][j] = str(mat[i][j] * scalar)

# print(mat)

for row in mat:
  # row = list(map(str, row))
  print(' '.join(row))
