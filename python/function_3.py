# solves a quadratic equation in the form ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
  inside = b**2 - (4 * a * c)
  if (inside < 0):
    return None
  elif (inside == 0):
    return [-4/(2 * a)]
  else:
    return [(-b + inside**0.5) / (2 * a), (-b - inside**0.5) / (2 * a)]

print(solve_quadratic(1, 5, 6))
