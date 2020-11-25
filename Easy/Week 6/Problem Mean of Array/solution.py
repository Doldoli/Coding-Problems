'''
Week 6 - Problem Mean of Array
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an integer array arr, return the mean of the remaining integers after removing the smallest 5% and the largest 5% of the elements.
'''

from typing import List


# O(n * log(n)) time complexity, O(1) space complexity
def solution(array: List[int]) -> float:
    if len(array) == 0: return 0.0

    num = len(array) // 20
    array.sort()
    if num > 0:
        array = array[num:len(array) - num]
        return sum(array) / len(array)
    else:
        return sum(array) / len(array)


# Example usage
if __name__ == "__main__":
    array = [
        4, 8, 4, 10, 0, 7, 1, 3, 7, 8, 8, 3, 4, 1, 6, 2, 1, 1, 8, 0, 9, 8, 0, 3, 9, 10, 3, 10, 1, 10, 7, 3, 2, 1, 4, 9,
        10, 7, 6, 4, 0, 8, 5, 1, 2, 1, 6, 2, 5, 0, 7, 10, 9, 10, 3, 7, 10, 5, 8, 5, 7, 6, 7, 6, 10, 9, 5, 10, 5, 5, 7,
        2, 10, 7, 7, 8, 2, 0, 1, 1
    ]
    result = solution(array)
    print(result)
