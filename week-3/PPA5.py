# n = 5
# for i in range(n):
#   x = int(input())
#   if x > max:
#     max = x

max = 0

while True:
  x = int(input())

  if x == 0:
    break

  if x > max:
    max = x

print(max)
