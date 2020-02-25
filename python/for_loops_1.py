# m is a list of integers
m = [5,7,6,8,1,4,2,7]

# here number is just a variable name 
# the for loop iterates each item in list m 
# the print statement prints the number and the number squared
for number in m:
  print(number, number**2)

# here i is a variable for the list index 
# the for loop iterates from 0 (first item) 
#  through len(m) which is the last item
# the print statement prints the index i, 
# and the i'th item in the list, m[i]
print()
for i in range(len(m)):
  print(i, m[i])
