
def is_palindrome(num):
  num = str(num)
  reversed_num = num[::-1]

  if num == reversed_num:
    return True
  else:
    return False

n = int(input("Enter a number for palindrome check: "))

print(f"\nRESULT:")
if is_palindrome(n):
  print(f"The number is a palindrome number.\n")

else:
  print(f"The number is not a palindrome number\n")
