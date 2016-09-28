x = 0
y = 1
z = 0
EfibTotal = 0

while x < 4000000:
  x = y + z
  z = y
  y = x
  if x % 2 == 0:
    EfibTotal += x

print(EfibTotal)