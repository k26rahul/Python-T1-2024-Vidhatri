total_marks = int(input())
total_options = int(input())
correct_options = list(map(int, input().split(',')))
selected_options = list(map(int, input().split(',')))

marks = 0

for opt in selected_options:
  if opt in correct_options:
    marks += total_marks/len(correct_options)

print(marks)
