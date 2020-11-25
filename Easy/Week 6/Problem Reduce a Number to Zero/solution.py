'''
Week 6 - Problem Product and Sum of Digits
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given a non-negative integer num, return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''


# O(n) time complexity, O(1) space complexity
def solution(num: int) -> int:
    count = 0
    while num > 0:
        if num % 2 == 0: num /= 2
        else: num -= 1
        count += 1
    return count


# Example usage
if __name__ == "__main__":
    num = 12345
    result = solution(num)
    print(result)