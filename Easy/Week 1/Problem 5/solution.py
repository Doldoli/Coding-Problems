'''
Week 1 - Problem 5 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given a sorted array nums, remove the duplicates such that 
each element appears only once and returns the new length.
'''

from typing import List

array = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 10, 10, 3453, 3453, 1]


# Solution 1: 0(n) time complexity, O(n) space complexity
def solution(array: List[int]) -> List[int]:
    res = []
    for i in array:
        if i not in res:
            res.append(i)
    return res


# Solution 2: O(n) time complexity, O(n) space complexity
solution_2 = list(set(array))

# Example usage
if __name__ == "__main__":
    solution_1 = solution(array)
    print(solution_1)
    print("----------------------")
    print(solution_2)