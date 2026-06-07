
def find(n):
  nums = []
  for i in range(n):
    x = int(input("enter number: "))
    nums.append(x)

  largest = max(nums)
  print(f"\nLargest: {largest}\n")


n = int(input(f"\nHow many number you have: "))

if n>0:
  find(n)
else:
  print(f"Err0: Wrong input(value is must greater than 1)")


