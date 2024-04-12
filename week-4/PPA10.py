n = int(input())

mat_a = []
mat_b = []

for i in range(n):
  row = list(map(int, input().split(',')))
  mat_a.append(row)

for i in range(n):
  row = list(map(int, input().split(',')))
  mat_b.append(row)

# print(f'{mat_a=}')
# print(f'{mat_b=}')

ans_mat = [[
    0 for i in range(n)
] for i in range(n)]

for i in range(n):
  for j in range(n):
    ans_mat[i][j] = str(mat_a[i][j] + mat_b[i][j])

# print(ans_mat)

for row in ans_mat:
  print(','.join(row))
