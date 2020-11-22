'''
Week 2 - Problem Contiguous Subarray
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an integer array, find the contiguous subarray which has the largest sum and return the sum.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(array: List[int]) -> int:
    if len(array) <= 1: return array[0]
    sum, best = 0, array[0]

    for i in range(len(array)):
        sum = max(array[i], array[i] + sum)
        best = max(sum, best)
    return best


# Example usage
if __name__ == "__main__":
    array = [1, -4, -1, 3, 2, 6, -2, -1, 3, -1, -3, 5, -9, 9, -2, 8, -1, 2, -3, 2]
    result = solution(array)
    print(result)