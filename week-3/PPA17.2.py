word_1 = input()
word_2 = input()

new_word = ''
n = len(word_1) + len(word_2)

for i in range(n):
  if len(word_1) == 0:
    new_word += word_2
    break

  if len(word_2) == 0:
    new_word += word_1
    break

  digit_1 = word_1[0]
  digit_2 = word_2[0]

  if digit_1 < digit_2:
    new_word += digit_1
    word_1 = word_1[1:]

  if digit_2 < digit_1:
    new_word += digit_2
    word_2 = word_2[1:]

  if digit_1 == digit_2:
    new_word += digit_1 + digit_2
    word_1 = word_1[1:]
    word_2 = word_2[1:]

print(new_word)
