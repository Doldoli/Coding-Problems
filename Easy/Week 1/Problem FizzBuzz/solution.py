'''
Week 1 - Problem FizzBuzz
@author: André Gilbert, andre.gilbert.77110@gmail.com

Output the string representation of numbers from 1 to n
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.
'''

from typing import List


# O(n) time complexity, O(n) space complexity
def solution(n: int) -> List[int]:
    ans = []

    for i in range(1, n + 1):

        div_by_3 = (i % 3 == 0)
        div_by_5 = (i % 5 == 0)

        if div_by_3 and div_by_5:
            ans.append("FizzBuzz")
        elif div_by_5:
            ans.append("Buzz")
        elif div_by_3:
            ans.append("Fizz")
        else:
            ans.append(str(i))
    return ans


# Example usage
if __name__ == "__main__":
    n = 30
    result = solution(n)
    print(result)