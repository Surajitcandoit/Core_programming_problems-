
def if_leapYear(y):
  if y%400 == 0 or (y%100 != 0 and y%4 == 0):
    return True
  else:
    return False


year = int(input("Enter a year to check: "))

if if_leapYear(year):
  print(f"Yes, its a Leap Year\n")
else:
  print(f"Nope!, its not a Leap Year\n")

