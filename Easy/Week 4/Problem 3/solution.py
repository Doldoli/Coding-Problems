'''
Week 4 - Problem 3 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array nums of size n, find the majority element. 
The majority element is the element that appears more than n/2 times.
'''

from typing import List
from collections import Counter


# O(n) time complexity, O(n) space complexity
def solution_1(nums: List[int]) -> int:
    count = Counter(nums)
    return (max(count.keys(), key=count.get))


# O(n) time complexity, O(1) space complexity
def solution_2(nums: List[int]) -> int:
    count = 0
    number = None

    for num in nums:
        if count == 0:
            number = num
        count += (1 if num == number else -1)
    return number


# Example usage
if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result_1 = solution_1(nums)
    print(result_1)
    print("---")
    result_2 = solution_2(nums)
    print(result_2)
