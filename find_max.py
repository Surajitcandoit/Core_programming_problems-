#O(n)
def easy_find(nums):
  return max(nums)

#O(log n)
def two_pointer(nums):
  left = 0
  right = len(nums) - 1
  max = 0
  for i in range(len(nums)):
    if nums[left] <= nums[right]:
      max = nums[right]
      left += 1
    else:
      max = nums[left]
      right -= 1

  return max

#O(n)
def linear_search(nums):
  max = nums[0]
  for i in nums:
    if i > max:
      max = i
  return max

#O(n log n)
def hacker_find(nums):
  nums.sort()
  return nums[-1]



n = int(input("How many element you have: "))
nums = []
for i in range(n):
  num = int(input("Enter element: "))
  nums.append(num)

print(f"\nLargest among those is:")
print("Easy way: ", easy_find(nums))
print("Two-pointer method: ", two_pointer(nums))
print("Linear Search: ", linear_search(nums))
print("Hacker mode: ", hacker_find(nums))

