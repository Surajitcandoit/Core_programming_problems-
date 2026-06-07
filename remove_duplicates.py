nums = [3,4,5,9,6,3,7,2,1,3]

#O(n)
def easy_way(arr=None):
    if arr is None:
        arr = nums
    result = []
    seen = set()
    for i in arr:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result
#    return list(dict.fromkeys(arr))


#O(n²)
def manual(arr=None):
    if arr is None:
        arr = nums.copy()
    else:
        arr = arr.copy()

    i = 0
    while i < len(arr):
        j = i + 1

        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1

        i += 1

    return arr

try:

    n = int(input("Enter how many elements: "))
    arrn = list(map(int, input().split()))
    if len(arrn) != n:
        print("Invalid number of elements!")
    else:
        print(f"\nBefore remove duplicates: {arrn}")
        print(f"\nAfter remove duplicates: ")
        print(easy_way(arrn))
        print(manual(arrn))
except ValueError:
    print("Please enter valid integers! code run with default value.")
    print(f"\nBefore remove duplicates: {nums}")
    print(f"\nAfter remove duplicates: ")
    print(easy_way())
    print(manual())
