n = int(input())

for x in range(1, n-2):
  for y in range(x+1, n-1):
    for z in range(y+1, n):
      eq = x**2 + y**2 == z**2
      if eq:
        print(f'{x},{y},{z}')
