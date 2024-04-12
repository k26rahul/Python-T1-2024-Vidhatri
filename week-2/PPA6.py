word = input()
n = len(word)

if n % 2 == 0:
  if word[-1] == '.':
    word = word[:-1]
    n -= 1
  else:
    word = word + '.'
    n += 1

left = (n - 3)//2
# print(word[:left])
print(word[left:left+3])
# print(word[left+3:])
