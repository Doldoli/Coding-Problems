'''
Week 6 - Problem Find even Numbers
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array of integers, return the count of even numbers.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution_1(array: List[int]) -> int:
    count = 0
    for num in array:
        if len(str(num)) % 2 == 0:
            count += 1
    return count


# O(n) time complexity, O(1) space complexity
def solution_2(array: List[int]) -> int:
    return sum(map(lambda num: 1 - len(str(num)) % 2, array))


# Example usage
if __name__ == "__main__":
    array = [1, 4, 13084, 322, 3420108, 24320913, 223233, 12, 5365, 894, 139, 87954]
    result_1 = solution_1(array)
    result_2 = solution_2(array)
    print(result_1)
    print("---")
    print(result_2)