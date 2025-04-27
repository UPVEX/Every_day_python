"""
search_range
    [5, 7, 7, 8, 8, 8, 10], 8 ==>[3, 5]
    [5, 7, 7, 8, 8, 8, 10],11 ==>[None, None]

"""

def search_range(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high-low) // 2
        if target < nums[mid]:
            high = mid + 1
        elif target > nums[mid]:
            low = mid + 1
        else:
            break

    for j in range(len(nums)-1, -1, -1):
        if nums[j] == target:
            return [mid , j]

    return [None, None]

print(search_range([5, 7, 7, 8, 8, 8, 10], 8))
print(search_range([5, 7, 7, 8, 8, 8, 10],11))