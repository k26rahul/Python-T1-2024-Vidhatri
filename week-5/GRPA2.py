n = int(input())

factors = []

for i in range(1, n):
  if n % i == 0:
    factors.append(i)

print(sum(factors) == n)
