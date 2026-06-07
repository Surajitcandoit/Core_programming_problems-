
num = int(input("Enter a number: "))

def d_count(n):
  n = abs(n) #to avoid skip negetive number
  u_digit = set()
  digit = 0
  oddCount = 0
  evenCount = 0
  if n == 0:
    digit = 1
    u_digit.add("0")
    evenCount = 1
    return [len(u_digit), digit, evenCount, oddCount]

  while n>0:
    rem = n%10
    n = n//10
    digit += 1  #count digit
    u_digit.add(rem)

    if what_digit(rem): #check even / odd
      evenCount += 1
    else:
      oddCount += 1

  return [len(u_digit), digit, evenCount, oddCount]

def what_digit(n):
  if n%2 == 0:
    return True
  else:
    return False


result = d_count(num)

print(f"Your number contains {result[1]} Digit and have {result[0]} unique Digit.\n")
print(f"Even digit: {result[2]}\nOdd digit: {result[3]}")

