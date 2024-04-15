words = []

while True:
  word = input()

  if word == 'STOP':
    break

  words.append(word)


print(f'{words}')
