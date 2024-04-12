word = input()

all_vowels_cond = 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word
first_app_cond = False
count_cond = False

if all_vowels_cond:
  first_app_cond = word.index('a') < word.index('e') < word.index('i') \
      < word.index('o') < word.index('u')

  count_cond = word.count('a') >= word.count('e') >= word.count('i') \
      >= word.count('o') >= word.count('u')

if all_vowels_cond and first_app_cond and count_cond:
  print('It is a perfect word')
else:
  print('It is not a perfect word')
