
def nsum(n):
  sum = 0
  while n > 0:
    sum = sum + n
    n -= 1
  return sum

n = int(input("Enter a number: "))

if n>0:
  result = nsum(n)
  print(f"Sum of {n} numbers: {result}\n")
else:
  result = 0
  print(f"Sum of {n} numbers: {result}\n")
