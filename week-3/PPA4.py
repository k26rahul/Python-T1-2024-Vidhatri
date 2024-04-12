n = int(input())

is_prime = True

for i in range(2, n):  # range [2, n-1]
  if n % i == 0:
    is_prime = False
    break

if is_prime:
  print('PRIME')
else:
  print('NOTPRIME')
