'''
Week 1 - Problem 3
@author: André Gilbert, andre.gilbert.77110@gmail.com

Find cumulative sum of a list.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(array: List[int]) -> List[int]:
    for i in range(1, len(array)):
        array[i] += array[i - 1]
    return array


# Example usage
if __name__ == "__main__":
    array = [4, 10, 15, 18, 20, 1, 23, 534, 6, 23, 1, 66435, 42, 23, 546, 7, 76, 45, 867, 45654, 7657, 254, 6, 5]
    result = solution(array)
    print(result)
