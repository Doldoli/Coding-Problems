'''
Week 2 - Problem Rotate Array
@author: André Gilbert, andre.gilbert.77110@gmail.com

Write a programm that rotates an array of size n by d elements.
'''

from typing import List


# O(n) time complexity, O(1) space complexity
def solution(array: List[int], d: int, n: int) -> None:
    for i in range(gcd(d, n)):
        temp = array[i]
        j = i

        while 1:
            k = j + d
            if k >= n:
                k = k - n

            if k == i:
                break

            array[j] = array[k]
            j = k
        array[j] = temp


# greatest common divisor
def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# Example usage
if __name__ == "__main__":
    array = [2, 3, 2, 3, 12, 4, 6, 7, 4, 9]
    d = 5
    solution(array, d, len(array))
    print(array)
