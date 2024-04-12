word1 = input()
word2 = input()

if len(word1) != len(word2):
  print(-1)
else:
  n = len(word1)

  dist_sum = 0
  for i in range(n):
    letter1 = word1[i]
    letter2 = word2[i]
    dist = abs(ord(letter1) - ord(letter2))
    dist_sum += dist

  print(dist_sum)
