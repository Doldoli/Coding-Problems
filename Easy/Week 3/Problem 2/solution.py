'''
Week 3 - Problem 2 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given an array, design an algorithm to find the maximum profit.
Note that you can't sell a stock before you buy one and you are only permitted to complete at most one transaction.
'''


# O(n) time complexity, O(1) space complexity
def solution(s: str) -> bool:
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]


# Example usage
if __name__ == "__main__":
    string_1 = "Hello"
    string_2 = "Race a car"
    string_3 = "A man, a plan, a canal: Panama"
    result_1 = solution(string_1)
    result_2 = solution(string_2)
    result_3 = solution(string_3)
    print(result_1)
    print("-----")
    print(result_2)
    print("-----")
    print(result_3)