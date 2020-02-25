# find the largest of 3 numbers

x, y, z = 6, 3, 8

largest = x
if y > x and y > z:
  largest = y
elif z > x and z > y:
  largest = z

print(largest)
