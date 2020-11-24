'''
Week 5 - Problem Intersection of Two Arrays 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given two arrays, write a function to compute their intersection.
'''

from typing import List


def helper_func(set_1, set_2):
    return [x for x in set_1 if x in set_2]


# O(n + m) time complexity, O(n + m) space complexity
def solution_1(array_1: List[int], array_2: List[int]) -> List[int]:
    set_1 = set(array_1)
    set_2 = set(array_2)

    if len(set_1) < len(set_2):
        return helper_func(set_1, set_2)
    else:
        return helper_func(set_2, set_1)


# O(n + m) average time complexity -> O(n * m) worst time complexity, O(n + m) space complexity
def solution_2(array_1: List[int], array_2: List[int]) -> List[int]:
    set_1 = set(array_1)
    set_2 = set(array_2)
    return list(set_2 & set_1)


# Example usage
if __name__ == "__main__":
    array_1 = [4, 9, 5, 1, 3, 4, 9, 7]
    array_2 = [9, 4, 9, 8, 4, 7, 3]
    result_1 = solution_1(array_1, array_2)
    result_2 = solution_2(array_1, array_2)
    print(result_1)
    print("-----------------------")
    print(result_2)
