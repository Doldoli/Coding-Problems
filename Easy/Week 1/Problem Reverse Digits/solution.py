'''
Week 1 - Problem Reverse Digits
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array of integers, reverse the digits.
'''

from typing import List


# O(n^2) time complexity, O(1) space complexity
def solution(array: List[int]) -> List[int]:
    for i in range(0, len(array)):
        if array[i] >= 0:
            array[i] = int(str(array[i])[::-1])
        else:
            array[i] = int('-' + str(array[i])[::-1][:-1])
    return array


# Example usage
if __name__ == "__main__":
    array = [140, 124, -89]
    result = solution(array)
    print(result)