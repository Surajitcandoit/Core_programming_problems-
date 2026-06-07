
def print_fib(n):
  fib = 0
  n_fib = 1
  print(fib)
  print(n_fib)

  i = 2
  while i<n:
    temp = fib
    fib = n_fib
    n_fib = temp + fib
    print(n_fib)

    i += 1

def pyth_fib(n):
  a, b = 0, 1
  for _ in range(n):
    print(a)
    a, b = b, a+b


n = int(input("Enter a number: "))
print(f"First {n} fibonacci in static method:")
print_fib(n)

print(f"\nFirst {n} fibonacci in pythonic method:")
pyth_fib(n)


