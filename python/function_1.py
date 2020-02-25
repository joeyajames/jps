# A SIMPLE FUNCTION - decides whether a text string starts with the letter a
def starts_with_a(x):
  if x.startswith('a') or x.startswith('A'):
    return True
  else:
    return False

print('ash', starts_with_a('ash'))
print('3.14', starts_with_a('3.14'))
print('six', starts_with_a('six'))
print('Apple', starts_with_a('Apple'))
