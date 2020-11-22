'''
Week 1 - Problem Nested List
@author: André Gilbert, andre.gilbert.77110@gmail.com

Change the given list into a nested list.
'''

from typing import List

array = ['Python', 'Java', 'R', 'C#', 'Typescript', 'C++', 'Golang', 'PHP', 'Javascript', 'Kotlin', 'Swift']
nums_of_elements = 5


# Solution 1: O(n^2) time complexity, O(1) space complexity
def solution(array: List[str], n: int) -> List[str]:
    for i in range(0, len(array), n):
        yield array[i:i + n]


# Solution 2: O(n^2) time complexity, O(1) space complexity
solution_2 = [array[i:i + nums_of_elements] for i in range(0, len(array), nums_of_elements)]

# Example Usage
if __name__ == '__main__':
    solution_1 = list(solution(array, nums_of_elements))
    print(solution_1)
    print("------------------------------------------------------------------")
    print(solution_2)
