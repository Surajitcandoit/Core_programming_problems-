
def is_armstrong(num):
  num = str(num)
  power = length(num)
  sum = 0
  for i in num:
    sum = sum + pow(int(i), power)

  if sum == int(num):
    return True
  else:
    return False


print(f"Check your number is Armstrong or not.\n")
n = int(input("Enter a number: "))

print("\nResult:")
if is_armstrong(n):
  print("Your number is a Armstromg number\n")

else:
  print("Your number is not a Armstromg number\n")

