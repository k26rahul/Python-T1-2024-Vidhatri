L = list(map(float, input().split(',')))

max_L = L[0]
for x in L:
  if x > max_L:
    max_L = x

min_L = L[0]
for x in L:
  if x < min_L:
    min_L = x

print(max_L - min_L)
