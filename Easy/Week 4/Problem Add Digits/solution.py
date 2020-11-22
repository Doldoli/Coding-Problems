'''
Week 4 - Problem Add Digits
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
'''


# O(1) time complexity, O(1) space complexity
def solution_1(num: int) -> int:
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9


# O(1) time complexity, O(1) space complexity
def solution_2(num: int) -> int:
    return 1 + (num - 1) % 9 if num else 0


# Example usage
if __name__ == "__main__":
    num = 47
    result_1 = solution_1(num)
    print(result_1)
    print("-----------")
    result_2 = solution_2(num)
    print(result_2)
