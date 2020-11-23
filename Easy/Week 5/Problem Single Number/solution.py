'''
Week 5 - Problem Single Element 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given a non-empty array of integers, every element appears twice except for one. Find the single number.
'''

from typing import List
from collections import defaultdict


# O(n) time complexity, O(n) space complexity
def solution_1(array: List[int]) -> int:
    hash_map = defaultdict(int)
    for i in array:
        hash_map[i] += 1

    for i in hash_map:
        if hash_map[i] == 1:
            return i


# O(n) time complexity, O(n) space complexity
def solution_2(array: List[int]) -> int:
    return 2 * sum(set(array)) - sum(array)


# O(n) time complexity, O(1) time complexity
def solution_3(array: List[int]) -> int:
    a = 0
    for i in array:
        a ^= i
    return a


# Example usage
if __name__ == "__main__":
    array = [1, 2, 2, 1, 6, 3, 5, 3, 5, 7, 8, 8, 7]
    result_1 = solution_1(array)
    result_2 = solution_2(array)
    result_3 = solution_3(array)
    print(result_1)
    print("---")
    print(result_2)
    print("---")
    print(result_3)
