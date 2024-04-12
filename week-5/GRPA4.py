n = int(input())

matrix = []

for i in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)

# calc row_sums
row_sums = [sum(row) for row in matrix]

# calc col_sums
col_sums = []
for j in range(n):
  j_col = [row[j] for row in matrix]
  col_sums.append(sum(j_col))

# calc d1_sum
d1 = []
for i in range(n):
  for j in range(n):
    if i == j:
      d1.append(matrix[i][j])
d1_sum = sum(d1)

# calc d2_sum
d2 = []
for i in range(n):
  for j in range(n):
    j_off = (n-1) - i
    if j == j_off:
      d2.append(matrix[i][j])
d2_sum = sum(d2)

# check if everything equals
check_1 = False
check_2 = False
check_3 = False

if row_sums == col_sums:
  check_1 = True

if d1_sum == d2_sum:
  check_2 = True

if d1_sum == row_sums[0]:
  check_3 = True

if check_1 and check_2 and check_3:
  print('YES')
else:
  print('NO')
