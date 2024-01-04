import collections
def min_operations_empty_array(nums: list) -> int:
    store = dict(collections.Counter(nums))
    temp = list(store.values())
    count = 0
    for i in temp:
        if i == 1:
            return -1
        count += i // 3
        if i%3:
            count += 1
    return count

print(min_operations_empty_array([2,2,3,3]))

# Approach is to take the maximum operator allowed to performa operation i.e. 3
# Count occurences of int
# If occurence equals 1 return -1
# Increase count by dividing occurence by 3. This is done to get the nearest possible value till which the occurence can be solved by the 3 operator
# Increase count by 1 if the occurence modulo 3 is more than 0. This is done to check if anything is remaining then in that case add it to the count.
# Example take occurence 7. 2+2+3. From our logic 7//3 will give us 2 and then 7%4 will give us 1. So we tried to get to the closes possible multiple of 3 and in that process calculated the number of 2 operator's operations.
# Then the remaining 3 operator's operation was calculated.