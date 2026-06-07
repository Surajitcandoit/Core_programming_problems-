#function to check prime
def is_prime(num):
  if num < 2:
    return False

  for i in range(2, num):
    if num%i == 0:
      return False

  return True

#taking limits
low = int(input("Lower range: "))
high = int(input("Upper range: "))

print(f"All prime number in range {low} to {high}:")

#check if num is zero or negative
if low < 0:
  print("Err(value): value cannot be negative.")
  exit()

#if positive check
for i in range(low, high):
  if is_prime(i):
    print(i)


