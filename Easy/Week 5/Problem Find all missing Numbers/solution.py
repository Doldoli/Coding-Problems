'''
Week 5 - Problem Find all missing Numbers
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array of integers, some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
'''

from typing import List


# O(n) time complexity, O(n) space complexity
def solution(array: List[int]):
    ans = []
    set_num = set(array)

    for i in range(1, len(array)):
        if i not in set_num:
            ans.append(i)
    return ans


# Example usage
if __name__ == "__main__":
    array = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution(array)
    print(result)
