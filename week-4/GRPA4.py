names = input().split(',')
dobs = input().split(',')

n = len(names)

for i in range(n):
  name = names[i]
  dob = dobs[i]
  for j in range(i+1, n):
    partner_name = names[j]
    partner_dob = dobs[j]
    if dob == partner_dob:
      if name < partner_name:
        pair = (name, partner_name)
      else:
        pair = (partner_name, name)
      print(','.join(pair))
