n = int(input())

matrix = []

for i in range(n):
  row = list(map(int, input().split(',')))
  matrix.append(row)

print(f'{matrix=}')
