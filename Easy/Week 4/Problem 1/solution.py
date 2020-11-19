'''
Week 4 - Problem 1 
@author: André Gilbert, andre.gilbert.77110@gmail.com

Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.
'''


# O(n) time complexity, O(1) space complexity
def solution(s: str) -> int:
    s = s.strip()
    lst = s.split(" ")
    return len(lst[-1])


# Example usage
if __name__ == "__main__":
    s = "Hello World"
    result = solution(s)
    print(result)
