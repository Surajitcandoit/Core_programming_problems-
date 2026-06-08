
def find_missing(nums):
  low = min(nums)
  high = max(nums)
  num_set = set(nums)
  missing = []
  for i in range(low, high):
    if i not in num_set:
      missing.append(i)
  return missing


def one_missing(nums):
  if min(nums) != 1:
    return "Input is not a valid 1..N sequence."

  missing_list = find_missing(nums)
  if len(missing_list) == 1:
    return missing_list[0]

  elif len(missing_list) > 1:
    return "Multiple missing numbers found!"

  else:
    return "No missing number."


n = input("Enter your list of number space separately: ").strip()

try:
  nums = [int(x) for x in n.split()]
  print("Missing number is: ")
  print(one_missing(nums))
except ValueError:
  print("Enter integer value only!")