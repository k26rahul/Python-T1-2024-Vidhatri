n = int(input())

matrix_a = []
for i in range(n):
  row = list(map(int, input().split(',')))
  matrix_a.append(row)
print(f'{matrix_a=}')

matrix_b = []
for i in range(n):
  row = list(map(int, input().split(',')))
  matrix_b.append(row)
print(f'{matrix_b=}')
