'''
Week 5 - Problem Reverse String List 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Write a function that reverses a string. The input string is given as an array of characters char[].
'''

from typing import List


# O(n) time complexity, O(n) space complexity
def solution_1(array: List[str]) -> None:
    def helper_func(low: int, hi: int):
        if low < hi:
            array[low], array[hi] = array[hi], array[low]
            helper_func(low + 1, hi - 1)

    helper_func(0, len(array) - 1)


# O(n) time complexity, O(1) space complexity
def solution_2(array: List[str]) -> None:
    low, hi = 0, len(array) - 1
    while low < hi:
        array[low], array[hi] = array[hi], array[low]
        low, hi = low + 1, hi - 1


# O(n) time complexity, O(1) space complexity
def solution_3(array: List[str]) -> None:
    array.reverse()


# Example usage
if __name__ == "__main__":
    array = ["P", "y", "t", "h", "o", "n"]
    solution_1(array)
    # solution_2(array)
    # solution_3(array)
    print(array)
