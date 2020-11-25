'''
Week 6 - Problem Product and Sum of Digits
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
'''


# O(n) time complexity, O(1) space complexity
def solution(num: int) -> int:
    product, sum = 1, 0

    for i in str(num):
        product *= int(i)
        sum += int(i)
    return product - sum


# Example usage
if __name__ == "__main__":
    num = 4421
    result = solution(num)
    print(result)