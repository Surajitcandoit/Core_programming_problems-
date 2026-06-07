
def nfact(n):
  fact = 1
  while n >= 1:
    fact *= n
    n -= 1
  return fact

n = int(input("Enter a number: "))
result = nfact(n)

print(f"Factorial of {n} = {result}.\n")
