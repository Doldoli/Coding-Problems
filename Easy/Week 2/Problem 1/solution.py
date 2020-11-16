'''
Week 2 - Problem 1 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array and a value, remove all instances of that value in-place and return the new length.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(array: List[int], value: int) -> int:
    while value in array:
        array.remove(value)
    return len(array)


# Example usage
if __name__ == "__main__":
    array = [12, 1, 23, 12, 4, 2, 1, 23, 4, 4, 5, 2, 7]
    value = 4
    result = solution(array, value)
    print(result)