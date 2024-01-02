import collections
def array_2darray_conditions(nums: list[int]) -> list:
    store = collections.Counter(nums)
    number_rows = max(store.values())
    result = [[] for _ in range(number_rows)]

    for num,count in store.items():
        for i in range(count):
            result[i].append(num)
    return result

print(array_2darray_conditions([1,3,4,1,2,3,1]))

# Approach is to create a hashmap of the number of times the integers appear in the given array
# Then use the hashmap to find out the maximum number of sub-arrays you need to store the number that occurs the most.
# Use the count of other numbers to keep their track and place them only once in each sub array.
