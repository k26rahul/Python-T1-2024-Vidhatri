def transpose(matrix):
  num_cols = len(matrix[0])

  transpose = []
  for j in range(num_cols):
    j_col = [row[j] for row in matrix]
    transpose.append(j_col)

  return transpose


# testing (not part of submitted sol)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

print(transpose(matrix))
