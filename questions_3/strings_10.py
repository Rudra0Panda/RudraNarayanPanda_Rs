def missing(nums):
    n = len(nums) + 1  
    sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return sum - actual_sum

nums = [1, 2, 4, 5, 6]
print(missing(nums))
