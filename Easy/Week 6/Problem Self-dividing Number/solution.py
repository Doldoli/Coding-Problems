'''
Week 6 - Problem Self-dividing Number 
@author: André Gilbert, andre.gilbert.77110@gmail.com

A self-dividing number is a number that is divisible by every digit it contains.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
The boundaries of each input argument are 1 <= left <= right <= 1000.
'''

from typing import List


# O(n) time complexity, O(n) space complexity
def solution(left: int, right: int) -> List[int]:
    def self_dividing(num: int) -> bool:
        for digit in str(num):
            if digit == '0' or num % int(digit) > 0:
                return False
        return True

    ans = []
    for num in range(left, right + 1):
        if self_dividing(num):
            ans.append(num)
    return ans


# Example usage
if __name__ == "__main__":
    left, right = 1, 100
    result = solution(left, right)
    print(result)
