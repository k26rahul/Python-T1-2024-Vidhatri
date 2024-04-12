n = int(input())

scores_dataset = []

for i in range(n):
  name = input()
  city = input()
  seq_no = int(input())
  marks_p = int(input())
  marks_c = int(input())
  marks_m = int(input())

  entry = {
      'Name': name,
      'City': city,
      'SeqNo': seq_no,
      'Mathematics': marks_m,
      'Physics': marks_p,
      'Chemistry': marks_c,
  }

  scores_dataset.append(entry)

# print(scores_dataset)
