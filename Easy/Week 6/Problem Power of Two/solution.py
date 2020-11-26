'''
Week 6 - Problem Minimum Time Visiting All Points
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
'''


# O(n) time complexity, O(1) space complexity
def solution_1(num: int) -> bool:
    i = 0
    while 2**i <= num:
        if 2**i == num: return True
        else: i += 1
    return False


# O(1) time complexity, O(1) space complexity
def solution_2(num: int) -> bool:
    return num > 0 and num & (num - 1) == 0


if __name__ == "__main__":
    num = 18446744073709551616
    result_1 = solution_1(num)
    result_2 = solution_2(num)
    print(result_1)
    print("-----")
    print(result_2)