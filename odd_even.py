
def what_digit(num):
  if num%2 == 0 or num == 0:
    print(f"The number is Even\n")
  else:
    print(f"The number is Odd\n")


n = int(input(f"\nEnter the number: "))

what_digit(n)
