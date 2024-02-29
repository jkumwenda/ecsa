# Solution utilising lists.

# def two_sum_list(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []


# Solution utilising sets:

# def two_sum_set(nums, target):
#     seen = set()
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [nums.index(complement), i]
#         seen.add(num)
#     return []


# COMPARISON:

# 1.Time Complexity:

# The solution using lists has a time complexity of O(n^2) due to the nested loop.
# The solution using sets has a time complexity of O(n) since it iterates through the array only once.

# 2.Space Complexity:

# The solution using lists has a space complexity of O(1) as it doesn't use any additional data structures.
# The solution using sets has a space complexity of O(n) because it uses a set to store the seen numbers.

# 3. Efficiency:

# The solution using sets is generally more efficient for large arrays because of its linear time complexity.

# REASONS TO PREFER ONE OVER THE OTHER:

# 1. Use Lists When:

# Memory usage is a concern, and the array is small.
# There is no need for optimizing time complexity.

# 2. Use Sets When:

# Time complexity is crucial, especially for large arrays.
# Memory usage is not a significant concern.

# ALTERNATIVE SOLUTION:

# You can use a hash map to store the indices of seen numbers, also providing a solution with O(n) time complexity.


def two_sum_hash_map(nums, target):
    num_indices = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_indices:
            return [num_indices[complement], i]

        num_indices[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
result_indices = two_sum_hash_map(nums, target)
print(result_indices)

# This solution operates efficiently with a time complexity of O(n), indicating that the time required for solving the problem grows linearly with the size of the array. It traverses the array just once, examining each element only once. The algorithm utilizes a hash map to store the indices of numbers it has encountered, contributing to a space complexity of O(n) where the amount of additional memory used scales linearly with the array size. The hash map aids in swiftly determining if a number's complement (the number needed to reach the target sum) has been seen before. In simpler terms, this approach intelligently tracks numbers as it moves through the array, providing an effective solution for identifying two numbers that sum up to a given target.
