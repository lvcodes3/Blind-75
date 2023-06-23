"""
3. CONTAINS DUPLICATE

Given an array of integers, return true if any value appears at least twice in the array
return false if every element is distinct

Ex: [1, 2, 3, 1]
Sol: true

Ex: [1, 2, 3, 4]
Sol: false
"""

from typing import List

# Time Complexity: O(n) bc we only iterate through the array once
# Memory: O(n) bc we created a hash-map which can hold up to n elements
def main(nums: List[int]) -> bool:
    num_dict = {}

    # loop through array
    for num in nums:
        if num in num_dict:
            return True
        else:
            num_dict[num] = ""

    return False

# Test Case
nums_1 = [1, 2, 3, 1]
nums_2 = [1, 2, 3, 4]

print(main(nums_1))
print(main(nums_2))