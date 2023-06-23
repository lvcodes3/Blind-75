"""
2. BEST TIME TO BUY AND SELL STOCK  

Say we have an array for which the ith element is the price of a given stock on day i

If we are only permitted to complete at most 1 transaction (buy one and sell one share of the stock)
design an algorithm to find the max profit (you can't sell a stock before you buy one)

Ex: [7, 1, 5, 3, 6, 4]
Sol: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6) => profit = 6 - 1 = 5
"""

from typing import List

# Time Complexity: O(n) bc we only scan through the array one time
# Memory: O(1) bc we only used 2 pointers and not another array
def main(nums: List[int]) -> int:
    left = 0 # buy pointer
    right = 1 # sell pointer
    maxProfit = 0

    # loop until right is out of bounds
    while right < len(nums):
        # if profitable, calculate the profit
        if nums[left] < nums[right]:
            profit = nums[right] - nums[left]
            maxProfit = max(maxProfit, profit)
        # if not profitable, update the index of the buy pointer to be at the new lowest point (sell pointer)
        else:
            left = right
        # regardless move sell pointer forward
        right += 1
    
    return maxProfit

# Test Case
number_arr = [7, 1, 5, 3, 6, 4]

print(main(number_arr))

