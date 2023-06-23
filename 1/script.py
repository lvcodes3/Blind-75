"""
1. TWO SUM

Given an array of integers, return indices of the two numbers such that they add up to the specific target.

Assume each input has exactly 1 solution, and we may not use the same element twice.

Ex: [2, 7, 11, 15], target = 9
Sol: [0, 1] bc 2 + 7 = 9
"""

from typing import List, Tuple
# Array in Python is a List 
# Tuple in Python is an ordered, immutable sequence of elements

# Brute Force Solution
# O(n^2) time complexity bc uses two for loops
def solution_one(nums: List[int], target: int) -> Tuple[int, int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
        
# Linear Solution
# O(n) time complexity bc only uses one for loop
def solution_two(nums: List[int], target: int) -> Tuple[int, int]:
    # create an empty dictionary to store numbers as keys and their indices as values
    num_dict = {}

    # enumerate through the elements of the nums list along with their indices
    for i, num in enumerate(nums):
        # calculate the complement of the current number to find the desired sum
        complement = target - num

        # check if complement exists as a key in the dictionary
        if complement in num_dict:
            # if the complement is found, return the indices of the current number and its complement
            return num_dict[complement], i
        
        # if the complement is not found, add the current number and its index to the dictionary
        num_dict[num] = i

# Test Case
number_arr = [2, 7, 11, 15]
target = 9

print("First Solution")
print(solution_one(number_arr, target))

print("Second Solution")
print(solution_two(number_arr, target))