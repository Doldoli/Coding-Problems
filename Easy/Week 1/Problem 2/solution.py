'''
Week 1 - Problem 2  
@author: André Gilbert, andre.gilbert.77110@gmail.com

Find N largest elements from a list.
'''

from typing import List


# O(n*log(n)) time complexity, O(1) space complexity
def solution(array: List[int], n: int) -> List[int]:

    # For practice implement a sorting algorithm yourself
    array.sort()
    return array[-1:-n - 1:-1]


# Example usage
if __name__ == "__main__":
    array = [81, 52, 45, 10, 3, 2, 96, 123, 100, 43, 30, 15, 95, 32, 46, 74, 80, 12, 32, 44, 11, 22, 88, 90, 121, 56]
    n = 3
    result = solution(array, n)
    print(result)