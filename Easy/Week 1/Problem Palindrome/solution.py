'''
Week 1 - Problem Palindrome
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array of integers. Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same forward as backward.
'''

from typing import List


# O(n^2) time complexity, O(1) space complexity
def solution(array: List[int]) -> List[bool]:
    for i in range(0, len(array)):
        if array[i] < 0:
            array[i] = False

        forward = str(array[i])
        backward = forward[::-1]

        if forward == backward:
            array[i] = True
        else:
            array[i] = False
    return array


# Example usage
if __name__ == "__main__":
    array = [12321, -343, 1230]
    result = solution(array)
    print(result)
