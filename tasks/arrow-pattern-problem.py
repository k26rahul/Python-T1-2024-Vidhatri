n = 7
mid = (n+1)/2
for i in range(n):
  main = '*' * (n-i)

  if i < mid:
    print(main.rjust(n))

  else:
    out = '*'.rjust(n-i)
    out += main.rjust(i)
    print(out)
