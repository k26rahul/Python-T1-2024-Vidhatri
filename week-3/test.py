# n = 6

# for i in range(n):
#   name = input()
#   print(f'hello {name}')

# while True:
#   name = input()

#   if name == 'STOP':
#     break

#   print(f'hello {name}')

# stop_found = False

# while not stop_found:
#   name = input()

#   if name == 'STOP':
#     stop_found = True

#   print(f'hello {name}')

for i in range(10**5):
  print(f'loop is running {i}th itr')

  name = input()

  if name == 'STOP':
    break  # it's time to break/stop the loop

  print(f'hello {name}')
