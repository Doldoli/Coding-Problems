'''
Week 3 - Problem Maximum Profit
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array, design an algorithm to find the maximum profit.
Note that you can't sell a stock before you buy one and you are only permitted to complete at most one transaction.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(prices: List[int]) -> int:
    output = 0
    if not prices: return output
    min_cost = float("inf")

    for i in range(len(prices)):
        if prices[i] < min_cost:
            min_cost = prices[i]
        elif prices[i] - min_cost > output:
            output = prices[i] - min_cost
    return output


# Example usage
if __name__ == "__main__":
    prices = [7, 4, 9, 10, 3, 8, 1, 6, 1, 2, 8, 1, 4, 2, 7, 1, 3, 5]
    result = solution(prices)
    print(result)