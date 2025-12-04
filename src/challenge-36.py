"""a
"""

segment1 = float(input("Type the first segment: "))
segment2 = float(input("Type the second segment: "))
segment3 = float(input("Type the third segment: "))

if segment1 < segment2 + segment3 and segment2 < segment1 + segment3 and segment3 < segment1 + segment2:
  print("The segment above can form a triangle!")
else:
  print("The segment above can not form a triangle!")