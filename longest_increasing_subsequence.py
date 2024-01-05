def longest_increasing_subsequence(nums: list) -> int:
    LIS = [1] * len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)

print(longest_increasing_subsequence([10,9,2,5,3,7,101,10]))

# Approach is to begin the DP with the last element of the array. 
# Check whether the ith element is lesser than the element 1 ahead of it.
# If it isnt then we already have set the value as 1 when creating LIS
# If it is lesser than the element ahead of it then that gives us an increasing subsequence and so we assign it the value of the maximum between itslef and LIS[j]th element + 1 (including it)
# Finally we return the maximum value of LIS