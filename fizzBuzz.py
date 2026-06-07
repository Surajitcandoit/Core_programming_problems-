def fizzORbuzz(num, d1, d2):
  if num%d1 == 0 and num%d2 == 0:
    print("FizzBuzz")
  elif num%d1 == 0:
    print("Fizz")
  elif num%d2 == 0:
    print("Buzz")
  else:
    print("Faaaaaaaaaah!")

try:
  num = int(input("Enter a number: "))
  a = int(input("Enter first divisor: "))
  b = int(input("Enter second divisor: "))

  fizzORbuzz(num,a,b)

except ValueError:
  print("Enter valid integer number.")


