n = int(input())

matrix = []
for i in range(n):
  row = list(map(int, input().split()))
  matrix.append(row)
  # print(f'{row=}')

# print(f'{matrix=}')  # [[1, 2], [3, 4]]
print(matrix)
