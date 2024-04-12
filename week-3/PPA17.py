word_1 = input()
word_2 = input()

new_word = ''
n = len(word_1) + len(word_2)

for i in range(n):
  new_digit = None

  if len(word_1) > 0 and len(word_2) > 0 and \
          int(word_1[0]) < int(word_2[0]):
    new_digit = word_1[0]
    word_1 = word_1[1:]
  elif len(word_1) > 0 and len(word_2) > 0 and \
          int(word_2[0]) < int(word_1[0]):
    new_digit = word_2[0]
    word_2 = word_2[1:]

  if new_digit is not None:
    new_word += new_digit

print(new_word + word_1 + word_2)
