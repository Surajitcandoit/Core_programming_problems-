def find_two(nums, target):
  seen = {}
  for i in nums:
    rem = target - i
    if i in seen:
      return [seen[i], i]

    seen[rem] = i

print("Enter all element separate with space→")
nums = list(map(int, input().split()))

x = int(input("Enter your Sum value: "))
print("Two number are:")

result = find_two(nums, x)
if result != None:
  print(result)
else:
  print("Sum value is not possible with any two number.\nTry again!")

