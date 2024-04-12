coins = int(input())
share_1 = int(input())
share_2 = int(input())
share_3 = int(input())

# All three of them should get a non-zero share.
unfair_condition_1 = share_1 == 0 or share_2 == 0 or share_3 == 0

# No two of them should get the same number of coins.
unfair_condition_2 = share_1 == share_2 or share_1 == share_3 or share_2 == share_3

# You should not have any coins with you at the end of this sharing process.
unfair_condition_3 = share_1 + share_2 + share_3 != coins

if unfair_condition_1 or unfair_condition_2 or unfair_condition_3:
  print('UNFAIR')
else:
  print('FAIR')
